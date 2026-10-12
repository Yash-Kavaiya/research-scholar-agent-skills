#!/usr/bin/env python3
"""Small standard-library client for free scholarly APIs.

Sources: arXiv, Semantic Scholar, OpenAlex, PubMed (NCBI E-utilities), Crossref.
No API key is required. Optional environment variables raise rate limits:

    OPENALEX_MAILTO   contact email for the OpenAlex and Crossref polite pools
    S2_API_KEY        Semantic Scholar API key
    NCBI_API_KEY      NCBI E-utilities API key

Every search returns a list of paper dicts with the same keys:

    title, authors (list of str), year (int or None), venue, doi, url,
    abstract, citations (int or None), source, id

This file is the canonical copy. Skills carry their own copy as
scripts/_scholarly_api.py; run tools/sync_shared.py after editing it.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

USER_AGENT = "research-scholar-agent-skills/0.1 (https://github.com/Yash-Kavaiya/research-scholar-agent-skills)"
SOURCES = ("arxiv", "semantic_scholar", "openalex", "pubmed", "crossref")
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"


class ApiError(RuntimeError):
    """A scholarly API could not be reached or returned an error."""


# --------------------------------------------------------------------------- HTTP


def http_get(url: str, params: dict | None = None, headers: dict | None = None,
             retries: int = 3, timeout: int = 30) -> bytes:
    """GET with retry on 429 and 5xx. Raises ApiError on failure."""
    if params:
        clean = {k: v for k, v in params.items() if v is not None}
        url = url + ("&" if "?" in url else "?") + urllib.parse.urlencode(clean)
    if not url.lower().startswith("https://"):
        raise ApiError(f"refusing to fetch a non-HTTPS URL: {url}")
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, **(headers or {})})
    delay = 2.0
    last: Exception | None = None
    for attempt in range(retries):
        try:
            # The scheme is checked above, so file: and custom schemes cannot reach urlopen.
            with urllib.request.urlopen(request, timeout=timeout) as response:  # nosec B310
                return response.read()
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code == 404:
                raise ApiError(f"404 Not Found: {url}") from exc
            if exc.code not in (429, 500, 502, 503, 504):
                raise ApiError(f"HTTP {exc.code} from {url}") from exc
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last = exc
        if attempt < retries - 1:
            time.sleep(delay)
            delay *= 2
    raise ApiError(f"request failed after {retries} attempts: {url} ({last})")


def utf8_stdout() -> None:
    """Make printing non-ASCII titles safe on Windows consoles."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def get_json(url: str, params: dict | None = None, headers: dict | None = None) -> dict:
    return json.loads(http_get(url, params, headers).decode("utf-8"))


def _mailto() -> str | None:
    return os.environ.get("OPENALEX_MAILTO") or None


# --------------------------------------------------------------------- normalizing


def normalize_doi(doi: str | None) -> str:
    """Lowercase a DOI and strip resolver prefixes. Returns '' when absent."""
    if not doi:
        return ""
    doi = doi.strip().lower()
    doi = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", doi)
    return doi.rstrip(".,; ")


def normalize_title(title: str | None) -> str:
    """Lowercase, strip accents, LaTeX braces and punctuation, for matching titles."""
    if not title:
        return ""
    text = unicodedata.normalize("NFKD", title)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"\\[a-zA-Z]+", " ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text.lower())
    return " ".join(text.split())


def title_similarity(a: str | None, b: str | None) -> float:
    """Token Jaccard similarity of two titles after normalizing, from 0 to 1."""
    ta, tb = set(normalize_title(a).split()), set(normalize_title(b).split())
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def make_paper(**fields) -> dict:
    paper = {
        "title": "", "authors": [], "year": None, "venue": "", "doi": "", "url": "",
        "abstract": "", "citations": None, "source": "", "id": "",
    }
    paper.update(fields)
    paper["title"] = " ".join((paper["title"] or "").split())
    paper["abstract"] = " ".join((paper["abstract"] or "").split())
    paper["doi"] = normalize_doi(paper["doi"])
    paper["venue"] = paper["venue"] or ""
    if not paper["url"] and paper["doi"]:
        paper["url"] = "https://doi.org/" + paper["doi"]
    return paper


def dedupe(papers: list[dict]) -> list[dict]:
    """Merge records of the same paper (same DOI, or same normalized title).

    The first record wins; empty fields are filled from later duplicates and
    the highest citation count is kept. `sources` lists every source that
    returned the paper.
    """
    merged: list[dict] = []
    by_key: dict[str, dict] = {}
    for paper in papers:
        keys = [k for k in ("doi:" + paper["doi"] if paper["doi"] else "",
                            "title:" + normalize_title(paper["title"]) if paper["title"] else "") if k]
        existing = next((by_key[k] for k in keys if k in by_key), None)
        if existing is None:
            existing = dict(paper)
            existing["sources"] = [paper["source"]]
            merged.append(existing)
        else:
            for field, value in paper.items():
                if field == "citations":
                    if value is not None and (existing["citations"] is None or value > existing["citations"]):
                        existing["citations"] = value
                elif field != "source" and not existing.get(field) and value:
                    existing[field] = value
            if paper["source"] not in existing["sources"]:
                existing["sources"].append(paper["source"])
        for key in keys:
            by_key[key] = existing
    return merged


# -------------------------------------------------------------------------- arXiv


def parse_arxiv(xml_bytes: bytes) -> list[dict]:
    # Refuse documents that declare a DTD or entities, which is how XML expansion attacks are delivered.
    if b"<!DOCTYPE" in xml_bytes or b"<!ENTITY" in xml_bytes:
        raise ApiError("arXiv response contains a DTD or entity declaration; refusing to parse it")
    root = ET.fromstring(xml_bytes)  # nosec B314
    papers = []
    for entry in root.findall(ATOM + "entry"):
        url = (entry.findtext(ATOM + "id") or "").strip()
        published = entry.findtext(ATOM + "published") or ""
        papers.append(make_paper(
            title=entry.findtext(ATOM + "title") or "",
            authors=[(a.findtext(ATOM + "name") or "").strip() for a in entry.findall(ATOM + "author")],
            year=int(published[:4]) if published[:4].isdigit() else None,
            venue=(entry.findtext(ARXIV_NS + "journal_ref") or "arXiv").strip(),
            doi=entry.findtext(ARXIV_NS + "doi") or "",
            url=url,
            abstract=entry.findtext(ATOM + "summary") or "",
            source="arxiv",
            id=re.sub(r"v\d+$", "", url.rsplit("/abs/", 1)[-1]),
            published=published[:10],
        ))
    return papers


def search_arxiv(query: str, limit: int = 10, sort_by: str = "relevance") -> list[dict]:
    """sort_by: relevance, submittedDate, or lastUpdatedDate. `query` may use arXiv field syntax."""
    if not re.search(r"\b(all|ti|au|abs|cat|co|jr|rn|id):", query):
        # arXiv ORs bare words, which buries relevant papers; require every term instead.
        query = " AND ".join("all:" + term for term in query.split())
    xml_bytes = http_get("https://export.arxiv.org/api/query", {
        "search_query": query, "start": 0, "max_results": limit,
        "sortBy": sort_by, "sortOrder": "descending",
    })
    return parse_arxiv(xml_bytes)


# --------------------------------------------------------------- Semantic Scholar

S2_FIELDS = "paperId,title,authors,year,venue,externalIds,abstract,citationCount,url"


def _s2_headers() -> dict:
    key = os.environ.get("S2_API_KEY")
    return {"x-api-key": key} if key else {}


def parse_s2_paper(item: dict) -> dict:
    external = item.get("externalIds") or {}
    return make_paper(
        title=item.get("title") or "",
        authors=[a.get("name", "") for a in item.get("authors") or []],
        year=item.get("year"),
        venue=item.get("venue") or "",
        doi=external.get("DOI") or "",
        url=item.get("url") or "",
        abstract=item.get("abstract") or "",
        citations=item.get("citationCount"),
        source="semantic_scholar",
        id=item.get("paperId") or "",
    )


def parse_s2(data: dict) -> list[dict]:
    return [parse_s2_paper(item) for item in data.get("data") or [] if item]


def search_semantic_scholar(query: str, limit: int = 10, year: str | None = None) -> list[dict]:
    """year: '2023', '2020-2024', or '2021-'."""
    data = get_json("https://api.semanticscholar.org/graph/v1/paper/search", {
        "query": query, "limit": min(limit, 100), "fields": S2_FIELDS, "year": year,
    }, _s2_headers())
    return parse_s2(data)


def s2_paper(paper_id: str) -> dict:
    """paper_id: S2 id, 'DOI:10...', 'ARXIV:2106.01345', or 'CorpusId:...'."""
    quoted = urllib.parse.quote(paper_id, safe=":")
    return parse_s2_paper(get_json(f"https://api.semanticscholar.org/graph/v1/paper/{quoted}",
                                   {"fields": S2_FIELDS}, _s2_headers()))


def s2_links(paper_id: str, direction: str, limit: int = 100) -> list[dict]:
    """direction: 'citations' (papers citing this one) or 'references' (papers it cites)."""
    if direction not in ("citations", "references"):
        raise ValueError("direction must be 'citations' or 'references'")
    quoted = urllib.parse.quote(paper_id, safe=":")
    data = get_json(f"https://api.semanticscholar.org/graph/v1/paper/{quoted}/{direction}",
                    {"fields": S2_FIELDS, "limit": min(limit, 1000)}, _s2_headers())
    key = "citingPaper" if direction == "citations" else "citedPaper"
    return [parse_s2_paper(row[key]) for row in data.get("data") or [] if row.get(key)]


# ----------------------------------------------------------------------- OpenAlex


def abstract_from_inverted_index(index: dict | None) -> str:
    if not index:
        return ""
    positions = [(pos, word) for word, places in index.items() for pos in places]
    return " ".join(word for _, word in sorted(positions))


def parse_openalex_work(item: dict) -> dict:
    location = item.get("primary_location") or {}
    source = location.get("source") or {}
    return make_paper(
        title=item.get("title") or item.get("display_name") or "",
        authors=[(a.get("author") or {}).get("display_name", "") for a in item.get("authorships") or []],
        year=item.get("publication_year"),
        venue=source.get("display_name") or "",
        doi=item.get("doi") or "",
        url=location.get("landing_page_url") or item.get("id") or "",
        abstract=abstract_from_inverted_index(item.get("abstract_inverted_index")),
        citations=item.get("cited_by_count"),
        source="openalex",
        id=(item.get("id") or "").rsplit("/", 1)[-1],
        published=item.get("publication_date") or "",
        referenced_works=[w.rsplit("/", 1)[-1] for w in item.get("referenced_works") or []],
    )


def parse_openalex(data: dict) -> list[dict]:
    return [parse_openalex_work(item) for item in data.get("results") or []]


def openalex_get(path: str, params: dict | None = None) -> dict:
    """GET https://api.openalex.org/<path> with the polite-pool mailto when set."""
    return get_json("https://api.openalex.org/" + path.lstrip("/"), {**(params or {}), "mailto": _mailto()})


def search_openalex(query: str, limit: int = 10, filters: str | None = None, sort: str | None = None) -> list[dict]:
    """filters: OpenAlex filter string, e.g. 'from_publication_date:2024-01-01,type:article'."""
    data = openalex_get("works", {
        "search": query or None, "per-page": min(limit, 200), "filter": filters, "sort": sort,
    })
    return parse_openalex(data)


def openalex_work(work_id: str) -> dict:
    """work_id: OpenAlex id ('W2741809807') or a DOI."""
    if not re.match(r"^W\d+$", work_id):
        work_id = "https://doi.org/" + normalize_doi(work_id)
    return parse_openalex_work(openalex_get("works/" + urllib.parse.quote(work_id, safe=":/")))


# ------------------------------------------------------------------------- PubMed

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"


def parse_pubmed_summary(data: dict) -> list[dict]:
    result = data.get("result") or {}
    papers = []
    for uid in result.get("uids") or []:
        item = result.get(uid) or {}
        doi = next((i.get("value", "") for i in item.get("articleids") or [] if i.get("idtype") == "doi"), "")
        pubdate = item.get("pubdate") or ""
        papers.append(make_paper(
            title=(item.get("title") or "").rstrip("."),
            authors=[a.get("name", "") for a in item.get("authors") or []],
            year=int(pubdate[:4]) if pubdate[:4].isdigit() else None,
            venue=item.get("fulljournalname") or item.get("source") or "",
            doi=doi,
            url=f"https://pubmed.ncbi.nlm.nih.gov/{uid}/",
            source="pubmed",
            id=uid,
        ))
    return papers


def search_pubmed(query: str, limit: int = 10) -> list[dict]:
    """`query` may use PubMed syntax (MeSH terms, [tiab], boolean operators)."""
    key = os.environ.get("NCBI_API_KEY") or None
    found = get_json(EUTILS + "esearch.fcgi", {
        "db": "pubmed", "term": query, "retmax": limit, "retmode": "json", "sort": "relevance", "api_key": key,
    })
    ids = (found.get("esearchresult") or {}).get("idlist") or []
    if not ids:
        return []
    summary = get_json(EUTILS + "esummary.fcgi", {
        "db": "pubmed", "id": ",".join(ids), "retmode": "json", "api_key": key,
    })
    return parse_pubmed_summary(summary)


def pubmed_count(query: str) -> int:
    """Number of PubMed records matching a query, for reporting search yields."""
    found = get_json(EUTILS + "esearch.fcgi", {
        "db": "pubmed", "term": query, "retmax": 0, "retmode": "json",
        "api_key": os.environ.get("NCBI_API_KEY") or None,
    })
    return int((found.get("esearchresult") or {}).get("count") or 0)


# ----------------------------------------------------------------------- Crossref


def parse_crossref_work(item: dict) -> dict:
    authors = []
    for person in item.get("author") or []:
        name = " ".join(part for part in (person.get("given"), person.get("family")) if part)
        authors.append(name or person.get("name", ""))
    year = None
    for field in ("published-print", "published-online", "published", "issued", "created"):
        parts = ((item.get(field) or {}).get("date-parts") or [[None]])[0]
        if parts and parts[0]:
            year = int(parts[0])
            break
    return make_paper(
        title=(item.get("title") or [""])[0],
        authors=authors,
        year=year,
        venue=(item.get("container-title") or [""])[0],
        doi=item.get("DOI") or "",
        url=item.get("URL") or "",
        abstract=re.sub(r"<[^>]+>", " ", item.get("abstract") or ""),
        citations=item.get("is-referenced-by-count"),
        source="crossref",
        id=item.get("DOI") or "",
        type=item.get("type") or "",
        volume=item.get("volume") or "",
        issue=item.get("issue") or "",
        pages=item.get("page") or "",
        publisher=item.get("publisher") or "",
    )


def parse_crossref(data: dict) -> list[dict]:
    return [parse_crossref_work(item) for item in (data.get("message") or {}).get("items") or []]


def search_crossref(query: str, limit: int = 10) -> list[dict]:
    """Bibliographic search: works for free text and for pasted reference strings."""
    data = get_json("https://api.crossref.org/works", {
        "query.bibliographic": query, "rows": min(limit, 100), "mailto": _mailto(),
    })
    return parse_crossref(data)


def crossref_doi(doi: str) -> dict | None:
    """Look up one DOI. Returns None when Crossref has no record of it."""
    try:
        data = get_json("https://api.crossref.org/works/" + urllib.parse.quote(normalize_doi(doi), safe="/"),
                        {"mailto": _mailto()})
    except ApiError as exc:
        if str(exc).startswith("404"):
            return None
        raise
    return parse_crossref_work(data.get("message") or {})


# ------------------------------------------------------------------------ unified

_SEARCHERS = {
    "arxiv": search_arxiv,
    "semantic_scholar": search_semantic_scholar,
    "openalex": search_openalex,
    "pubmed": search_pubmed,
    "crossref": search_crossref,
}


def search_all(query: str, sources: tuple[str, ...] | list[str] = SOURCES, limit: int = 10,
               pause: float = 0.4) -> tuple[list[dict], dict[str, str]]:
    """Search several sources and merge duplicates.

    Returns (papers, errors). A source that fails is reported in `errors`
    (source name to message) rather than aborting the whole search.
    """
    papers: list[dict] = []
    errors: dict[str, str] = {}
    for index, source in enumerate(sources):
        if source not in _SEARCHERS:
            errors[source] = "unknown source"
            continue
        if index:
            time.sleep(pause)
        try:
            papers.extend(_SEARCHERS[source](query, limit=limit))
        except ApiError as exc:
            errors[source] = str(exc)
    return dedupe(papers), errors


def filter_years(papers: list[dict], year_from: int | None = None, year_to: int | None = None) -> list[dict]:
    kept = []
    for paper in papers:
        year = paper.get("year")
        if year is None and (year_from or year_to):
            continue
        if year_from and year < year_from:
            continue
        if year_to and year > year_to:
            continue
        kept.append(paper)
    return kept


def short_authors(authors: list[str], limit: int = 3) -> str:
    authors = [a for a in authors if a]
    if not authors:
        return "Unknown authors"
    if len(authors) <= limit:
        return ", ".join(authors)
    return f"{authors[0]} et al."


def to_markdown(papers: list[dict], abstract_chars: int = 0) -> str:
    """Numbered Markdown list of papers. abstract_chars > 0 adds a truncated abstract."""
    lines = []
    for number, paper in enumerate(papers, 1):
        cites = f", {paper['citations']} citations" if paper.get("citations") is not None else ""
        venue = f" *{paper['venue']}*." if paper.get("venue") else ""
        link = paper.get("url") or ""
        sources = ", ".join(paper.get("sources") or [paper.get("source", "")])
        lines.append(f"{number}. **{paper['title']}** ({paper.get('year') or 'n.d.'}). "
                     f"{short_authors(paper['authors']).rstrip('.')}.{venue} {link} [{sources}{cites}]")
        if abstract_chars and paper.get("abstract"):
            text = paper["abstract"]
            lines.append("   > " + (text[:abstract_chars].rstrip() + "…" if len(text) > abstract_chars else text))
    return "\n".join(lines)


# ------------------------------------------------------------------------- BibTeX


def parse_bibtex(text: str) -> list[dict]:
    """Parse BibTeX into [{'type', 'key', 'fields'}]; field names are lowercased, in file order.

    Handles nested braces, quoted values, bare numbers and macros, and `#`
    concatenation. @string macros are expanded; @comment and @preamble are skipped.
    """
    entries, pos = [], 0
    macros: dict[str, str] = {}
    while True:
        at = text.find("@", pos)
        if at == -1:
            break
        match = re.compile(r"@\s*([A-Za-z]+)\s*([{(])").match(text, at)
        if not match:
            pos = at + 1
            continue
        kind = match.group(1).lower()
        body, end = _balanced(text, match.end() - 1)
        pos = end
        if kind == "string":
            macros.update(_parse_fields(body, macros))
            continue
        if kind in ("comment", "preamble"):
            continue
        key, _, rest = body.partition(",")
        entries.append({"type": kind, "key": key.strip(), "fields": _parse_fields(rest, macros)})
    return entries


def _balanced(text: str, start: int) -> tuple[str, int]:
    """Content of the brace or parenthesis group opening at `start`, and the index after it."""
    opener = text[start]
    closer = "}" if opener == "{" else ")"
    depth, i = 0, start
    while i < len(text):
        ch = text[i]
        if ch == "\\":
            i += 2
            continue
        if ch == "{" or (opener == "(" and ch == "("):
            depth += 1
        elif ch == "}" or (opener == "(" and ch == ")"):
            depth -= 1
            if depth == 0 and ch == closer:
                return text[start + 1:i], i + 1
        i += 1
    return text[start + 1:], len(text)


def _parse_fields(body: str, macros: dict[str, str] | None = None) -> dict[str, str]:
    fields: dict[str, str] = {}
    i, n = 0, len(body)
    while i < n:
        match = re.compile(r"[\s,]*([A-Za-z][\w:.+-]*)\s*=\s*").match(body, i)
        if not match:
            break
        name, i = match.group(1).lower(), match.end()
        parts = []
        while i < n:
            if body[i] == "{":
                value, i = _balanced(body, i)
            elif body[i] == '"':
                j, depth = i + 1, 0
                while j < n and (body[j] != '"' or depth):
                    depth += (body[j] == "{") - (body[j] == "}")
                    j += 2 if body[j] == "\\" else 1
                value, i = body[i + 1:j], j + 1
            else:
                j = i
                while j < n and body[j] not in ",#\n":
                    j += 1
                value, i = body[i:j].strip(), j
                value = (macros or {}).get(value.lower(), value)
            parts.append(value)
            rest = re.compile(r"\s*#\s*").match(body, i)
            if not rest:
                break
            i = rest.end()
        fields[name] = " ".join("".join(parts).split())
    return fields


FIELD_ORDER = ["author", "editor", "title", "booktitle", "journal", "year", "month", "volume", "number", "pages",
               "publisher", "address", "organization", "school", "institution", "series", "edition", "howpublished",
               "eprint", "archiveprefix", "primaryclass", "doi", "url", "note"]


def format_bibtex(entries: list[dict]) -> str:
    """Write entries with one field per line, aligned, in a conventional field order."""
    blocks = []
    for entry in entries:
        names = sorted(entry["fields"], key=lambda f: (FIELD_ORDER.index(f) if f in FIELD_ORDER else len(FIELD_ORDER), f))
        width = max((len(name) for name in names), default=0)
        lines = [f"  {name.ljust(width)} = {{{entry['fields'][name]}}}," for name in names]
        blocks.append("@" + entry["type"] + "{" + entry["key"] + ",\n" + "\n".join(lines) + "\n}")
    return "\n\n".join(blocks) + "\n"


def bib_authors(author_field: str) -> list[str]:
    """Split a BibTeX author field on ' and ' (outside braces)."""
    names, depth, current = [], 0, []
    tokens = re.split(r"(\s+and\s+|[{}])", author_field or "")
    for token in tokens:
        if token == "{":
            depth += 1
        elif token == "}":
            depth -= 1
        if depth == 0 and re.fullmatch(r"\s+and\s+", token or ""):
            names.append("".join(current).strip())
            current = []
        else:
            current.append(token or "")
    if "".join(current).strip():
        names.append("".join(current).strip())
    return names


def surname(name: str) -> str:
    """Normalized family name from 'Last, First', 'First Last', or '{Corporate Name}'."""
    name = name.strip()
    if name.startswith("{") and name.endswith("}"):
        return normalize_title(name)
    family = name.split(",")[0] if "," in name else (name.split() or [""])[-1]
    return normalize_title(family).replace(" ", "")
