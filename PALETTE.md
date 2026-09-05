# Chartsmith Color Palette

## System Overview

Every chart uses a **two-layer color system**:

1. **Gray layer** — context, background data, "everything else"
2. **Accent layer** — one color family (dark + light variant) spotlighting the key insight

This is not a suggestion. It is the default. A chart with more than two color families
is almost certainly doing too much.

---

## Gray Palette (Context)

Use these for all non-highlighted data elements.

| Token | Hex | Usage |
|---|---|---|
| `GRAY_900` | `#333333` | Titles, primary text |
| `GRAY_700` | `#666666` | Axis labels, secondary text |
| `GRAY_500` | `#999999` | Context data (medium emphasis) |
| `GRAY_300` | `#C0C0C0` | Context data (low emphasis), gridlines |
| `GRAY_100` | `#E8E8E8` | Lightest context, area fills, backgrounds |

## Accent Palettes

Pick **one** accent palette per chart. Each has a dark (primary) and light (secondary) variant.

### Steel Blue (Default)

| Token | Hex | Usage |
|---|---|---|
| `ACCENT_DARK` | `#2B5C8A` | Primary highlight — the main story element |
| `ACCENT_LIGHT` | `#8FABBE` | Secondary highlight — supporting story element |

### Slate Navy

| Token | Hex | Usage |
|---|---|---|
| `ACCENT_DARK` | `#26456E` | Primary highlight |
| `ACCENT_LIGHT` | `#7B9DBF` | Secondary highlight |

### Maroon

| Token | Hex | Usage |
|---|---|---|
| `ACCENT_DARK` | `#8B2323` | Primary highlight (alerts, negative trends) |
| `ACCENT_LIGHT` | `#C4726C` | Secondary highlight |

### Teal

| Token | Hex | Usage |
|---|---|---|
| `ACCENT_DARK` | `#1A7A6D` | Primary highlight |
| `ACCENT_LIGHT` | `#6BB5A8` | Secondary highlight |

### Burnt Orange

| Token | Hex | Usage |
|---|---|---|
| `ACCENT_DARK` | `#C75B12` | Primary highlight (warnings, change) |
| `ACCENT_LIGHT` | `#E8A85C` | Secondary highlight |

---

## Usage Rules

### Rule 1: Gray First, Then Color

Start with everything in `GRAY_500`. Then ask: *what is the single most important thing
in this chart?* Color only that.

### Rule 2: One Accent Family Per Chart

If the chart compares two groups (e.g., "before vs after"), use `ACCENT_DARK` for one and
`GRAY_500` for the other — not two different accent families. The exception: when the chart
explicitly contrasts two narratives (e.g., "received vs processed") and both need emphasis.
In that case, use `ACCENT_DARK` + `GRAY_700` or a second accent sparingly.

### Rule 3: Light Variant for Area Fills

When filling areas (area charts, confidence bands, range shading), use `ACCENT_LIGHT` or
`GRAY_100` — never the dark variant, which overwhelms the chart.

### Rule 4: Text Matches Data

When labeling a highlighted element, use the same accent color for the label text.
When labeling a gray element, use `GRAY_700`.

### Rule 5: Divergent Data Gets Two Accents

For divergent bar charts, waterfall charts, or any chart showing positive vs negative:
- Positive / increase → `ACCENT_DARK` (steel blue or teal)
- Negative / decrease → Maroon `ACCENT_DARK` (`#8B2323`)

This is the **only** standard case where two accent families appear in one chart.

---

## Python Quick Reference

```python
GRAY = {
    900: "#333333",
    700: "#666666",
    500: "#999999",
    300: "#C0C0C0",
    100: "#E8E8E8",
}

ACCENT = {
    "steel_blue":    {"dark": "#2B5C8A", "light": "#8FABBE"},
    "slate_navy":    {"dark": "#26456E", "light": "#7B9DBF"},
    "maroon":        {"dark": "#8B2323", "light": "#C4726C"},
    "teal":          {"dark": "#1A7A6D", "light": "#6BB5A8"},
    "burnt_orange":  {"dark": "#C75B12", "light": "#E8A85C"},
}
```

## R Quick Reference

```r
gray <- list(
  g900 = "#333333",
  g700 = "#666666",
  g500 = "#999999",
  g300 = "#C0C0C0",
  g100 = "#E8E8E8"
)

accent <- list(
  steel_blue   = list(dark = "#2B5C8A", light = "#8FABBE"),
  slate_navy   = list(dark = "#26456E", light = "#7B9DBF"),
  maroon       = list(dark = "#8B2323", light = "#C4726C"),
  teal         = list(dark = "#1A7A6D", light = "#6BB5A8"),
  burnt_orange = list(dark = "#C75B12", light = "#E8A85C")
)
```
