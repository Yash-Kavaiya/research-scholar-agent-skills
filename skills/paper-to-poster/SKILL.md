---
name: paper-to-poster
description: Designs an academic conference poster from a paper, with a headline finding, a column layout sized to the conference's dimensions, cut-down text, enlarged figures, and a QR code, delivered as a LaTeX (tikzposter or beamerposter) or PowerPoint layout. Use when the user asks to "make a poster for my paper", "design a conference poster", "create an A0 research poster", "convert my paper to a poster", "what should go on my poster", or needs a poster layout for a symposium.
---

# Paper to Poster

A poster is read from two metres away, in under a minute, by someone deciding whether to stop. Design for that reader first, then for the one who stays to talk.

## When to use

- A paper or abstract was accepted as a poster.
- A departmental or symposium poster session.
- Redesigning a text-heavy poster.

Hand off instead for a talk (`paper-to-slides`) or a written summary (`paper-to-blog`).

## Inputs

- The paper, and its figures as vector files or source data.
- The conference's poster instructions: size (A0, A1, 36 × 48 in, or other), orientation, and any template or logo rules. Sizes differ by event; get them from the instructions.
- Institution logos and branding requirements.
- Output format: LaTeX or PowerPoint.
- Whether it will be printed on paper or fabric, or shown on a screen.

## Workflow

1. **Confirm size and orientation** from the conference. A portrait A0 and a landscape 48 × 36 in board need different layouts.
2. **Write the headline finding**: one sentence in plain language stating the main result ("A 10-minute warm-up cuts injury rates by a third in amateur runners"). It is the most prominent text after the title, or it is the title.
3. **Choose the content.** A poster holds about 300 to 800 words in total. Select:
   - The problem and why it matters: 2 to 3 sentences or bullets.
   - The approach: one diagram with a short caption.
   - The 2 or 3 key results: one figure each, each with a caption that states the finding.
   - Conclusions: 3 bullets.
   - Reference to the paper, QR code, contact, acknowledgements, funding.

   Leave out the literature review, full methods, and most tables. The presenter and the paper supply those.
4. **Lay out the grid.** Three columns for landscape, two or three for portrait, with reading order top to bottom, then left to right. Number the sections or use clear headings. Give the results the largest area and the centre position. Keep 30 to 40% of the area as white space.

   ```
   +--------------------------------------------------------------+
   | TITLE (or headline finding)            authors | logos | QR  |
   +------------------+-----------------------+-------------------+
   | 1 Problem        | 3 Key result          | 4 Second result   |
   | 2 Approach       |   (largest figure)    | 5 Conclusions     |
   |   (diagram)      |                       | Refs, contact     |
   +------------------+-----------------------+-------------------+
   ```

5. **Set type sizes for distance** (for A0; scale for other sizes): title 85 to 120 pt, headline finding 60 to 80 pt, section headings 44 to 60 pt, body text 28 to 36 pt, captions and references 20 to 24 pt. Sans-serif for body text, left-aligned, in short lines and bullets.
6. **Remake the figures** for the poster: large fonts, thick lines, few series, direct labels, a finding-stating caption (`publication-figure-maker`, `architecture-diagram-maker`). Vector graphics, or raster at 150 to 300 dpi at final printed size.
7. **Choose a restrained palette**: one or two accent colours on a light background, strong contrast between text and background, and colour-blind-safe series colours. No background photos behind text.
8. **Add a QR code** to the paper, code, or a project page, with a short readable URL beside it. Test that it scans.
9. **Build it** with `tikzposter` or `beamerposter` in LaTeX, or a single custom-sized slide in PowerPoint (Design → Slide Size → Custom). Use the conference or institution template if one is required.
10. **Check a proof.** View at 100% zoom, and print on A4: if body text is readable at arm's length on A4, it will read at A0. Check logos, names, affiliations, and that images are not pixelated. Export to PDF with fonts embedded.
11. **Prepare the pitch**: a 30-second and a 2-minute spoken summary for people who stop.

## Output format

- A content plan:

```markdown
## Poster plan: <title> (<size>, <orientation>)
Headline: <one sentence>
| Block | Content | Words | Visual |
Total words: <n>
```

- The poster source (`.tex` or `.pptx`) and the PDF at final size.
- The 30-second and 2-minute pitch scripts.
- A print checklist: size, bleed if the printer needs it, file format, deadline.

## Quality bar and pitfalls

- Take the dimensions from the conference instructions. A poster of the wrong size or orientation may not fit the board.
- The content comes from the paper. Do not round a result favourably for the headline or drop the condition it depends on.
- A shrunken paper is the most common bad poster. If it has paragraphs, cut more.
- Do not paste the abstract. The headline and conclusions replace it.
- Every figure needs a caption that says what it shows; viewers will not ask.
- Body text below about 24 pt at A0 cannot be read from where people stand.
- Use logos and images you are permitted to use, and follow the institution's branding rules.
- Compile or open the file and inspect it before delivering; say so if it could not be rendered.
- Printing takes time. Tell the user to check the print shop's turnaround before the travel date.

## Related skills

- `paper-summarizer` and `abstract-writer` to distil the headline and conclusions.
- `publication-figure-maker` and `architecture-diagram-maker` to remake visuals at poster scale.
- `paper-to-slides` for the talk version, and `paper-to-blog` for a page the QR code can point to.
- `latex-paper-formatter` for LaTeX build problems.
- `viva-defense-prep` to rehearse answers to questions at the poster.
