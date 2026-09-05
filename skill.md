---
description: "Generate publication-quality data visualizations. Infers chart types from data, produces Python (seaborn/matplotlib) or R (ggplot2) code with isolated user variables, following Storytelling with Data principles."
---

# Chartsmith

You are generating a data visualization. Follow this skill completely — it overrides your default charting instincts.

---

## Step 1: Understand the Data

Before choosing a chart type or writing any code, understand what you are working with.

**If the user provided a CSV or data file:**
1. Read the file. Inspect the first 20 rows and all column headers.
2. Identify column types: categorical, numeric (continuous), numeric (discrete), date/time, text.
3. Count unique values in categorical columns.
4. Note the shape: how many rows, how many columns.
5. Look for obvious grouping or time-series structure.

**If the user described data verbally:**
1. Clarify any ambiguity before proceeding.
2. Create a small representative dataset in the code to demonstrate the chart.

**If the user already knows what chart they want:** skip to Step 3.

---

## Step 2: Recommend Chart Types

Based on the data structure, recommend 1-2 chart types. Use this decision tree:

### Single numeric variable over time
→ **Line chart** (continuous) or **Bar chart** (discrete periods)
- If showing a range (min/max/avg): line with shaded band
- If showing cumulative progress: area chart

### Comparing categories
→ **Horizontal bar chart** (5+ categories) or **Vertical bar chart** (≤4 categories)
- Rank-order bars by value unless the categories have inherent order (e.g., months)
- For survey/Likert data: divergent stacked horizontal bar

### Multiple series over time
→ **Line chart** (≤4 series) or **Small multiples / faceted** (5+ series)
- If comparing start vs end only: **slope chart**
- Never use dual y-axes — stack panels vertically instead

### Part-to-whole composition
→ **Stacked bar chart** (over time) or **100% stacked bar** (comparing proportions)
- Never pie charts. Never donut charts.

### Sequential gains and losses
→ **Waterfall chart**
- For budget reconciliation, headcount math, funnel steps

### Relationship between two numeric variables
→ **Scatterplot**
- If the data maps to strategic quadrants: **2x2 matrix scatterplot** with quadrant labels
- Add reference lines (averages, benchmarks) where meaningful

### Flow between stages or categories
→ **Sankey diagram**

### Values across two categorical dimensions
→ **Heatmap**

Present your recommendation briefly: *"This data has [structure]. I recommend a [chart type] because [reason]. Here's an alternative: [chart type] if you want to emphasize [different aspect]."*

---

## Step 3: Ask Clarifying Questions (only if needed)

Only ask if genuinely ambiguous. You usually have enough to proceed. If you must ask, limit to:
- What is the key takeaway? (What should the reader walk away knowing?)
- Which items should be highlighted vs shown as context?
- Python or R?

Default to **Python** unless the user specifies R.

---

## Step 4: Generate the Code

### Code Structure

Every script follows this structure exactly:

```
# ============================================================
# CONFIGURATION — Edit these variables to customize your chart
# ============================================================

# --- DATA ---
(data source, column mappings)

# --- CONTENT ---
(title, subtitle, annotations, source line)

# --- STYLE ---
(colors, highlight items, font sizes)

# --- OUTPUT ---
(dimensions, DPI, output file path)

# ============================================================
# CHART CODE — Modify below for advanced customization
# ============================================================

(imports)
(base style setup)
(data loading/processing)
(chart construction)
(annotations and labels)
(save/show)
```

### Python Base Style

Apply this `rcParams` block at the top of every Python chart:

```python
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.edgecolor": GRAY_300,
    "axes.linewidth": 0.8,
    "axes.grid": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.spines.left": True,
    "axes.spines.bottom": True,
    "xtick.color": GRAY_700,
    "ytick.color": GRAY_700,
    "xtick.major.size": 0,
    "ytick.major.size": 0,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "text.color": GRAY_900,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 11,
    "figure.dpi": 150,
})
```

### R Base Theme

Apply this ggplot2 theme in every R chart:

```r
theme_chartsmith <- function(base_size = 12) {
  theme_minimal(base_size = base_size, base_family = "Helvetica") +
    theme(
      plot.title = element_text(face = "bold", size = rel(1.3), color = g900,
                                margin = margin(b = 4)),
      plot.subtitle = element_text(size = rel(0.95), color = g700,
                                   margin = margin(b = 16)),
      plot.caption = element_text(size = rel(0.75), color = g500,
                                  hjust = 0, margin = margin(t = 12)),
      axis.title = element_text(size = rel(0.9), color = g700),
      axis.text = element_text(size = rel(0.85), color = g700),
      axis.ticks = element_blank(),
      panel.grid.major.x = element_blank(),
      panel.grid.major.y = element_line(color = "#EEEEEE", linewidth = 0.4),
      panel.grid.minor = element_blank(),
      legend.position = "none",
      plot.margin = margin(20, 20, 20, 20),
      plot.title.position = "plot",
      plot.caption.position = "plot"
    )
}
```

---

## The Constitution

These ten principles govern every chart. When in doubt, refer back here.

### 1. Every Element Earns Its Place
Remove chart junk: borders, background fills, unnecessary gridlines, tick marks, 3D effects. If removing an element doesn't hurt comprehension, it was clutter.

### 2. Color Is Signal, Not Decoration
Default all data to gray. Apply at most one accent color pair (dark + light) to highlight the key insight. Gray = context. Color = "look here." The chart must read correctly in grayscale.

**Color tokens:**
- Context: `GRAY_100` (#E8E8E8) through `GRAY_900` (#333333)
- Default accent: Steel Blue — dark `#2B5C8A`, light `#8FABBE`
- Negative/alert: Maroon — dark `#8B2323`, light `#C4726C`
- See PALETTE.md for full set and alternative accent pairs

### 3. Label Data Directly
No legends. Place labels on or adjacent to data elements. Match label color to data color. If a legend is truly unavoidable, place it inline near the data.

### 4. Titles State the Insight
"Revenue grew 23% after the September campaign" — not "Revenue Over Time." Use a subtitle for time range, units, or source.

### 5. Annotate the "So What"
Add text callouts explaining why patterns exist and what the reader should do about it. Bold the key phrase. Keep annotations to one or two sentences. Use leader lines to connect annotations to data.

### 6. Build Visual Hierarchy Through Weight
Thick/saturated for the story, thin/desaturated for context. The reader's eye should land on the insight first.

### 7. Choose the Right Form
Use the chart selection guide in Step 2. Never use pie charts, donut charts, or dual-axis charts.

### 8. Isolate What the Reader Will Change
All configurable values at the top of the script in named variables grouped by purpose (DATA, CONTENT, STYLE, OUTPUT). Descriptive names: `ACCENT_DARK`, not `c1`.

### 9. Whitespace Is a Feature
Generous margins, padding between groups, space between labels and data. If elements feel crowded, make the chart larger or simpler.

### 10. Accessibility Is Non-Negotiable
WCAG AA contrast. Never rely on color alone. Minimum 10pt annotations, 12pt axis labels, 14pt+ titles. Legible sans-serif font.

---

## Chart-Type-Specific Instructions

### Bar Charts

**Horizontal bar (category comparison):**
- Sort by value (largest at top) unless categories have natural order
- Place value labels at bar ends, outside the bar, in matching color
- Highlight 1-3 key bars with `ACCENT_DARK`; the rest in `GRAY_300`
- Add right-margin annotations explaining highlighted items

**Stacked bar:**
- Use for part-to-whole over time
- Limit to 3-4 segments; collapse small categories into "Other"
- Label segments directly inside bars when space permits
- Use a gray scale for context segments, accent for the focus segment

**Dodged/grouped bar:**
- Use for comparing 2-3 groups across categories
- Limit to 2-3 groups — more than that becomes unreadable
- Use `ACCENT_DARK` vs `GRAY_500` for two-group comparison
- Place value labels above each bar

**Divergent bar:**
- Center at zero; positive values extend right, negative left
- Use accent color for positive, maroon for negative
- Label values at bar ends with +/- signs

### Line Charts

**Single or grouped lines:**
- Use solid lines; vary weight to show hierarchy (2.5pt main story, 1.5pt context)
- Label the final point of each series directly — no legend
- Use dots/markers only on the highlighted series or at key data points
- For the main story line: `ACCENT_DARK`, thicker. Context lines: `GRAY_300`, thinner

**Line with range band:**
- Shade the range (min/max or confidence interval) in `GRAY_100` or `ACCENT_LIGHT` with alpha
- Draw the central tendency (mean/median) as a solid dark line
- Label the band ends (MAX, MIN, AVG) at the left edge

**Slope chart:**
- Two vertical axes (start and end period) connected by lines
- Gray for all lines except the highlighted story
- Highlight with `ACCENT_DARK` (or maroon/orange for a negative story)
- Label both endpoints with category name and value
- Group related items with whitespace

### Area Charts

- Use `ACCENT_LIGHT` or `GRAY_100` for the fill, with a darker line along the top edge
- Never stack more than 2-3 areas — they become unreadable
- For single-series area: fill in `ACCENT_LIGHT`, line in `ACCENT_DARK`
- Add annotations pointing to notable peaks or valleys

### Waterfall Charts

- Starting and ending bars in `ACCENT_DARK`
- Increase steps in `ACCENT_LIGHT` (or teal)
- Decrease steps in maroon `ACCENT_DARK` (#8B2323)
- Connector lines between bars (thin, dashed, `GRAY_300`)
- Label each bar with its value, using +/- signs for increases/decreases
- Place category labels below each bar; group into sections ("Additions", "Deductions") if applicable

### Scatterplot (2x2 Matrix)

- Draw quadrant reference lines at meaningful thresholds (averages, benchmarks)
- Label quadrants in the corners (bold, `GRAY_700`)
- Default all points to `GRAY_500`
- Highlight key points in `ACCENT_DARK` with direct labels (name + value)
- Mark the reference point (benchmark, average) with a larger, darker dot
- Invert y-axis if "fewer is better" (as in the Knaflic issues example)

### Heatmap

- Use a sequential color scale from white → `ACCENT_DARK`
- Add value labels inside each cell
- Sort rows and columns by a meaningful metric (total, average) unless order is inherent
- Use thin white borders between cells

### Sankey Diagram

- Use `GRAY_300` for all flows except the highlighted path
- Highlight the key flow in `ACCENT_DARK` with partial transparency
- Label nodes directly
- Keep to 2-3 levels of depth; more becomes unreadable
- Note: Sankey in matplotlib requires `matplotlib.sankey` or a library like `plotly` — default to plotly for Sankey and note this in the code

---

## Output

### What to produce
1. **A complete, runnable script** (Python or R) with all configuration variables at the top
2. **The chart** — save to PNG by default (SVG if the user requests vector output)
3. If the user's context is an HTML artifact: produce the chart as an inline image or embedded SVG

### Python save block
```python
plt.tight_layout()
plt.savefig(OUTPUT_FILE, dpi=DPI, bbox_inches="tight", facecolor="white")
plt.show()
print(f"Chart saved to {OUTPUT_FILE}")
```

### R save block
```r
ggsave(output_file, plot = p, width = fig_width, height = fig_height, dpi = dpi, bg = "white")
cat(paste("Chart saved to", output_file, "\n"))
```

### File naming
Default output filename: `chart.png`. If the title suggests a better name, use it: `revenue_growth.png`, `headcount_waterfall.png`.

---

## When This Skill Fires

Activate when the user:
- Asks to create a chart, graph, plot, or visualization
- Provides a CSV or data file and asks to visualize it
- Asks to "plot", "chart", "graph", or "visualize" something
- Asks for a specific chart type (bar, line, waterfall, heatmap, scatterplot, Sankey, slope chart)
- Provides data and asks "what chart should I use?"

Do **not** activate for:
- Dashboard layout or multi-chart composition (unless individual charts within it)
- Interactive web-based visualizations (D3, Plotly interactive)
- Image generation or illustration
- Map / geographic visualizations
