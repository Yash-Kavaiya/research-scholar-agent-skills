# Submission compliance guide

## 1. Page-count conventions to confirm

| Question | Variation between venues |
|---|---|
| Are references counted? | Often excluded at conferences; included at some journals |
| Are appendices counted? | Often allowed after references without limit; some cap them or require a separate file |
| Are acknowledgements counted? | Sometimes excluded; sometimes only allowed at camera-ready |
| Ethics, limitations, broader impact sections | Some venues exclude them from the limit; others include them |
| Checklists | Usually excluded, appended after the references |
| Camera-ready extra page | Some venues allow one more page after acceptance |

## 2. Template tampering checks

Search the source for these and remove them unless the template provides them:

| Pattern | Effect |
|---|---|
| `\vspace{-` | Removes space |
| `\setlength{\textheight}`, `\textwidth`, margins | Changes the text block |
| `\baselinestretch`, `\linespread`, `setspace` | Changes line spacing |
| `\small` or `\footnotesize` around body text | Shrinks text |
| `\captionsetup` with skip changes | Shrinks caption spacing |
| `\titlespacing` | Shrinks heading spacing |
| `\looseness=-1` everywhere | Occasional use is common; widespread use is noticed |
| Modified `.sty` or `.cls` files | Violates the template |

## 3. Anonymisation checklist

| Item | Check |
|---|---|
| Author block | Removed or replaced by "Anonymous" as the template specifies |
| Self-citations | Third person; no "our previous work [3]" |
| Acknowledgements and funding | Removed for review |
| Links | Code and data through anonymising services; no personal or lab URLs |
| Figures and screenshots | No names, usernames, institution logos, file paths |
| PDF metadata | Author and title fields cleared or anonymous |
| Supplementary files | Same checks; check document metadata of Word and PDF files |
| Writing that identifies | "At <University> we ..." |

## 4. Fonts

| Problem | Cause | Fix |
|---|---|---|
| Type 3 fonts | matplotlib default, some PostScript figures | Set `pdf.fonttype` and `ps.fonttype` to 42 and regenerate; or use a TrueType output setting |
| Non-embedded fonts | Figures from some tools, PDF printers | Re-export with fonts embedded; regenerate with `pdflatex` |
| Missing glyphs | Unicode characters not in the font | Use LaTeX commands or a font with the glyph |

Check with `pdffonts paper.pdf`: every font should show `emb yes`, and no font should have type `Type 3`.

## 5. Figures and resolution

| Item | Guideline |
|---|---|
| Line art and charts | Vector (PDF, EPS) |
| Photographs and microscopy | 300 dpi or more at printed size |
| Mixed | 600 dpi or vector with raster layers |
| Colour | Readable in greyscale where print is greyscale |

## 6. References

- No undefined citations (`[?]`) or references (`??`).
- Consistent style; DOIs where the venue asks.
- Preprints replaced by published versions where available.
- No duplicate entries.

## 7. Camera-ready additions

| Item | Notes |
|---|---|
| Authors and affiliations | Exactly as registered in the submission system |
| Acknowledgements and funding | Restored |
| Copyright or licence block | Publisher-specific text or rights statement |
| Conference and DOI information | Inserted by the template or publisher |
| PDF metadata | Title and authors set (`\hypersetup{pdftitle={...}, pdfauthor={...}}`) |
| Validator | IEEE PDF eXpress, ACM TAPS, or the publisher's checker |
| Copyright form | Submitted before the deadline |
| Accessibility | Alt text, tagged PDF, or source files if the publisher requires |
| Required changes | Changes promised in the rebuttal or required by the meta-review |
| Supplementary and code | Final, de-anonymised links |

## 8. Last-hour checks

Open the final PDF and read the first page, all captions, and the reference list. Confirm the file uploaded is the file checked. Keep a copy of the submitted PDF and sources.
