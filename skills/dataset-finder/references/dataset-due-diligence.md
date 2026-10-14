# Dataset sources and due diligence

## 1. Where to search

| Source | Strength | How to search |
|---|---|---|
| Hugging Face Hub | Text, vision, audio, multimodal; dataset cards; download counts | Bundled script; filter by task and licence on the website |
| OpenML | Tabular data with standard tasks and benchmarks | Bundled script (name match), or the website's full search |
| Kaggle | Very broad, competition data, community uploads | `kaggle datasets list -s "<query>"` with the Kaggle CLI configured; website otherwise |
| UCI Machine Learning Repository | Classic tabular benchmarks | Website search |
| Papers with Code | Datasets linked to tasks and leaderboards | Browse by task to see which datasets papers report on |
| Zenodo, Figshare, Dryad, OSF, Dataverse | Data attached to papers | Search the archive; filter by resource type dataset |
| Google Dataset Search | Index across many repositories | Web search interface |
| Government open-data portals | Statistics, administrative records | data.gov, data.gov.in, data.europa.eu, national statistics offices |
| PhysioNet | Physiological signals and clinical data | Credentialed access for many datasets |
| The Cancer Imaging Archive | Medical imaging | Collection pages with licence terms |
| GEO, SRA, ENA | Genomics | Accession search |
| ICPSR, UK Data Service | Social science surveys | Registration often required |
| LDC, ELRA | Language resources | Licence fees for many |
| OpenNeuro | Neuroimaging | BIDS-formatted datasets |

## 2. Fit to the task

| Question | Why it matters |
|---|---|
| Does the label match the research question's outcome? | A proxy label changes what the study measures |
| Is the size enough for the method and the planned splits? | Small test sets give unstable estimates |
| Are standard splits provided? | Comparability with published results |
| Is the class balance known? | Affects metrics and sampling |
| Does the population or domain match the claimed scope? | Limits generalisation |
| How old is it, and has the phenomenon changed? | Temporal drift |
| Is it the benchmark most papers report on? | Required for comparison with prior work |

## 3. Licence

| Licence | Research use | Commercial use | Redistribution | Notes |
|---|---|---|---|---|
| CC0, public domain | yes | yes | yes | |
| CC BY | yes | yes | yes, with attribution | |
| CC BY-SA | yes | yes | yes, same licence | Derived data must carry it |
| CC BY-NC | yes | no | yes, non-commercial | Check whether the project counts as commercial |
| CC BY-ND | yes | yes | unmodified only | Derivatives restricted |
| ODbL | yes | yes | yes, share-alike for databases | |
| MIT, Apache 2.0 (applied to data) | yes | yes | yes | Unusual for data; read the terms |
| Research-only custom terms | usually | no | no | Read every clause |
| Data use agreement | as agreed | as agreed | usually no | Signed by the institution |
| None stated | unknown | unknown | unknown | Treat as not permitted |

The licence of the annotations may differ from the licence of the underlying content (for example images or text scraped from the web). Check both.

## 4. Access

| Level | Typical time | Action |
|---|---|---|
| Open download | immediate | Record version and date |
| Gated (accept terms online) | minutes to days | Accept terms with the account that will be cited |
| Credentialed (training plus application) | days to weeks | Complete required training; apply early |
| Data use agreement | weeks to months | Involve the research office |
| Request to authors | uncertain | Email with purpose; plan an alternative |

## 5. Provenance and ethics

| Question | Red flag |
|---|---|
| How was it collected? | Scraped without permission; unclear source |
| Did people consent to this use? | Personal data with no consent statement |
| Is it de-identified? | Free text, faces, voices, or rare attributes that re-identify people |
| Who annotated it, and how? | No annotation guidelines or agreement figures |
| Is there a datasheet or data card? | None, or one that omits collection details |
| Has it been withdrawn or deprecated? | Official deprecation notice; known problems reported |
| Does it encode bias? | Skewed demographics; documented harmful labels |

Datasets with personal, health, or biometric data usually need ethics approval even when public.

## 6. Quality checks after download

- Count items per split against the documentation.
- Check for duplicates within and across splits (exact and near-duplicate).
- Inspect a random sample of labels for errors.
- Check missing values and their pattern.
- Look at distributions by class and by subgroup.
- For text and images: language, length, resolution, file corruption.
- Record the checksum and version used.

## 7. Contamination with pretraining data

For evaluations of pretrained models, check whether the test set may appear in the pretraining corpus: search for exact test items online, look for the dataset in published pretraining corpus lists, and prefer test sets released after the model's training cutoff where this matters.

## 8. Citing data

Cite the dataset paper and, if available, the dataset's own DOI and version. State the licence and any access conditions in the paper's data section.

## 9. Recommendation reasoning

| Role | Choose |
|---|---|
| Primary | Matches the question, widely reported, licence fits the use |
| Secondary | Different domain or population, to test generality |
| Avoid | Licence conflict, deprecation, known leakage, or unverifiable provenance |
