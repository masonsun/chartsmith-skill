# Chartsmith Constitution

These principles govern every chart produced by Chartsmith. They are derived from
Cole Knaflic's *Storytelling with Data* and refined through practice. Principles are
ranked — when two conflict, the higher-numbered principle yields to the lower.

---

## 1. Every Element Earns Its Place

Remove anything that does not directly help the reader understand the data.

- No chart borders, background fills, or shadow effects
- No gridlines unless they materially aid value comparison — and when used, make them thin (#EEEEEE) and horizontal only
- No tick marks — use padding instead
- No 3D effects, gradients, or decorative shapes
- No dual-axis charts — use stacked panels (small multiples) instead

If you are unsure whether an element helps: remove it. If the chart is harder to read without it, add it back.

## 2. Color Is Signal, Not Decoration

The default state of all data is **gray**. Color enters only to say *"look here."*

- Render all bars, lines, and points in context gray by default
- Apply **at most one accent color pair** (a dark and light variant) to spotlight the key insight
- Gray = context, background, "everything else." Accent color = the story
- If a second narrative thread exists, introduce a second accent **sparingly** — and only when the first accent alone would confuse
- A chart must be fully comprehensible printed in grayscale; color reinforces meaning but never carries it alone

**Never** use a rainbow palette, cycle through many hues, or assign colors arbitrarily. If you find yourself reaching for a third color family, simplify the chart instead.

## 3. Label Data Directly

Legends force the reader's eye to bounce between the key and the data. Eliminate that friction.

- Place labels directly on or adjacent to the data points they describe
- Match label color to the data element's color
- If a legend is truly unavoidable (many overlapping series), place it inline near the data — never in a separate box in a corner
- For bar charts: place value labels at bar ends or inside bars
- For line charts: label the final point of each series

## 4. Titles State the Insight

The title is the first thing the reader sees. Use it to deliver the takeaway, not describe the chart type.

**Do:**
- "Revenue grew 23% after the September campaign"
- "More than 1/3 of projects are missing goals"
- "Please approve the hire of 2 FTEs"

**Don't:**
- "Revenue Over Time"
- "Q3 Bar Chart"
- "Project Status"

Use a **subtitle** for context the title cannot carry: time range, units, data source, or a secondary observation. The title is bold and large; the subtitle is lighter and smaller.

## 5. Annotate the "So What"

A chart without annotation is a chart without a point. Annotations answer: *what should the reader do with this information?*

- Add text callouts explaining **why** a pattern exists, not just **that** it exists
- Use leader lines or arrows to connect annotations to specific data points
- Bold the key phrase within an annotation for scannability
- Place annotations near the data they explain — not in a footnote
- Keep annotations concise: one or two sentences maximum

## 6. Build Visual Hierarchy Through Weight

Guide the reader's eye with deliberate contrast in size, weight, and intensity.

- **Thick lines / saturated colors** for the main story
- **Thin lines / desaturated grays** for context
- **Larger, bolder text** for the single most important number or label
- Use bold sparingly — when everything is bold, nothing is
- The reader's eye should land on the insight first, then explore context

## 7. Choose the Right Form

Match the chart type to the analytical question. The wrong form makes even clean data confusing.

| Question | Chart type |
|---|---|
| How does a value change over time? | Line chart |
| How do categories compare? | Horizontal bar chart |
| What is the part-to-whole breakdown? | Stacked bar chart |
| What are the sequential gains and losses? | Waterfall chart |
| How do two variables relate? | Scatterplot |
| How does a value flow between stages? | Sankey diagram |
| How do values distribute across two dimensions? | Heatmap |
| How did values change between two points? | Slope chart |

**Never use pie charts.** A bar chart is always clearer for part-to-whole comparisons. Donut charts inherit the same problem.

## 8. Isolate What the Reader Will Change

All user-configurable values live at the top of the script in clearly named variables grouped by purpose. The reader should be able to customize the chart without reading the implementation.

```
# --- DATA ---
# --- CONTENT (titles, labels, annotations) ---
# --- STYLE (colors, sizes, fonts) ---
# --- OUTPUT (file path, dimensions, DPI) ---
```

Variable names are descriptive (`ACCENT_DARK`, not `c1`). Group related settings. Comment only when the name alone is insufficient.

## 9. Whitespace Is a Feature

Generous spacing makes a chart feel calm and professional. Cramped charts feel urgent and amateurish.

- Ample margins around the plot area (especially top, for the title)
- Space between groups in grouped bar charts
- Padding between labels and data elements
- Let the data breathe — if elements feel crowded, the chart may need to be larger or simpler

## 10. Accessibility Is Non-Negotiable

Charts reach diverse audiences. Design for all of them.

- Maintain sufficient contrast ratios (WCAG AA minimum)
- Never rely on color alone to distinguish data — pair color with labels, patterns, or position
- Minimum font size: 10pt for annotations, 12pt for axis labels, 14pt+ for titles
- Use a legible sans-serif font (Helvetica, Arial, or system equivalent)
- Test: can someone describe this chart accurately from a black-and-white printout?
