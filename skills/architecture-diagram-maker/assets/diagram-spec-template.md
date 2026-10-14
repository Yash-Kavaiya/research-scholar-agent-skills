# Diagram spec: <figure label>

**Message:** <the one idea the reader should take away>
**Format:** TikZ | Mermaid | Graphviz | SVG   **Width:** one column | full width
**Direction:** left to right | top to bottom

## Elements

| ID | Label (as in the text) | Kind | Style | Novel? |
|---|---|---|---|---|
| x | <...> | data / module / operator / storage / decision | <...> | no |

## Connections

| From | To | Kind | Label |
|---|---|---|---|
| x | enc | data flow / gradient / optional | <tensor or shape> |

## Groups

| Group | Members | Label |
|---|---|---|

## Legend

- <shape or colour>: <meaning>

## Caption

> <what the diagram shows; how to read it; what is new>

## Assumptions made where the description was incomplete

- <...>

## Checks

- [ ] Names match the method section
- [ ] Compiles and renders; inspected at print size
- [ ] Greyscale readable
