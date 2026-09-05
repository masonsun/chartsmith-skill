# Chartsmith

A Claude Code skill for generating publication-quality data visualizations. Feed it a CSV or describe your data — it infers the right chart type, then produces clean, tweakable Python or R code that follows the principles from Cole Knaflic's *Storytelling with Data*.

## What it does

1. **Reads your data** — CSV files, dataframes, or verbal descriptions
2. **Recommends a chart type** — bar, line, waterfall, slope, scatterplot, heatmap, or Sankey based on data structure
3. **Generates runnable code** — Python (seaborn/matplotlib) or R (ggplot2) with all user-configurable values isolated at the top
4. **Follows a design constitution** — 10 principles that produce clean, honest, story-driven charts every time

## The Constitution (summary)

1. Every element earns its place — no chart junk
2. Color is signal, not decoration — gray for context, one accent pair for the story
3. Label data directly — no legends
4. Titles state the insight — not "Revenue Over Time" but "Revenue grew 23%"
5. Annotate the "so what"
6. Visual hierarchy through weight
7. Choose the right form
8. Isolate what the reader will change
9. Whitespace is a feature
10. Accessibility is non-negotiable

See [CONSTITUTION.md](CONSTITUTION.md) for the full principles.

## Install

Copy the skill file into your Claude Code skills directory:

```bash
# Project-level (recommended)
mkdir -p .claude/skills
cp skill.md .claude/skills/chartsmith.md

# Global (available in all projects)
mkdir -p ~/.claude/skills
cp skill.md ~/.claude/skills/chartsmith.md
```

## Usage

Once installed, Chartsmith activates automatically when you ask Claude Code to create a visualization:

```
> Visualize this CSV as a bar chart highlighting the top 3 categories

> Here's my quarterly revenue data — what chart should I use?

> Create a waterfall chart showing our headcount changes this year

> /chartsmith
```

### What you get

A complete, runnable script with this structure:

```python
# ============================================================
# CONFIGURATION — Edit these variables to customize your chart
# ============================================================

# --- DATA ---
DATA_FILE = "revenue.csv"

# --- CONTENT ---
TITLE = "Revenue grew 23% after the September campaign"
SUBTITLE = "Monthly revenue, Jan–Dec 2024"

# --- STYLE ---
ACCENT_DARK = "#2B5C8A"
HIGHLIGHT_ITEMS = ["September", "October"]

# --- OUTPUT ---
OUTPUT_FILE = "revenue_growth.png"

# ============================================================
# CHART CODE
# ============================================================
...
```

Change the variables at the top. Run the script. Get a publication-ready chart.

## Color System

Every chart uses a two-layer system:

- **Gray layer** — context, background data, "everything else"
- **Accent layer** — one color family (dark + light) spotlighting the key insight

| Role | Default | Hex |
|---|---|---|
| Context (light) | Light gray | `#C0C0C0` |
| Context (medium) | Medium gray | `#999999` |
| Accent (primary) | Steel blue dark | `#2B5C8A` |
| Accent (secondary) | Steel blue light | `#8FABBE` |
| Negative/alert | Maroon | `#8B2323` |

Five accent palettes ship by default (steel blue, slate navy, maroon, teal, burnt orange). See [PALETTE.md](PALETTE.md) for the full reference.

## Supported Chart Types

| Chart | Variants |
|---|---|
| Bar | Horizontal, vertical, stacked, dodged, divergent, 100% stacked |
| Line | Single, grouped, faceted, with range band |
| Slope | Two-period comparison |
| Area | Single, stacked |
| Waterfall | Sequential gains and losses |
| Scatterplot | Standard, 2x2 matrix with quadrant labels |
| Heatmap | Sequential color scale with value labels |
| Sankey | Flow between stages |

## Examples

The `examples/python/` directory contains complete scripts reproducing charts from *Storytelling with Data*:

- `bar_horizontal.py` — Top 10 design concerns (Figure 4.9)
- `bar_stacked.py` — Goal attainment over time (100% stacked)
- `line_annotated.py` — Ticket volume with contextual annotation
- `waterfall.py` — Headcount math
- `slope_chart.py` — Employee feedback over time
- `scatterplot_2x2.py` — Satisfaction vs issues matrix (Figure 5.6)

## License

MIT — see [LICENSE](LICENSE).

## Acknowledgments

Design principles adapted from Cole Knaflic's [*Storytelling with Data*](https://www.storytellingwithdata.com/). Chartsmith is an independent project, not affiliated with or endorsed by the author.
