"""
Chartsmith — Stacked Bar Chart
Inspired by: Knaflic "Goal attainment over time"

100% stacked bar showing composition over time with annotation callout.
"""

# ============================================================
# CONFIGURATION — Edit these variables to customize your chart
# ============================================================

# --- DATA ---
periods = ["Q1\n2013", "Q2", "Q3", "Q4", "Q1\n2014", "Q2", "Q3", "Q4",
           "Q1\n2015", "Q2", "Q3"]

# Each segment: (label, values_list, color)
# Values should be percentages that sum to ~100 per period
segments = [
    ("Exceed", [40, 35, 28, 25, 20, 18, 15, 12, 10, 8, 5], "#666666"),
    ("Meet",   [55, 60, 68, 72, 72, 73, 73, 73, 70, 59, 53], "#C0C0C0"),
    ("Miss",   [5,  5,  4,  3,  8,  9,  12, 15, 20, 33, 42], "#8B2323"),
]

# --- CONTENT ---
TITLE = "Goal attainment over time"
SUBTITLE = ""
SOURCE = "Data source: XYZ Dashboard; the total number of projects has increased over time from 230 in early 2013 to nearly 270 in Q3 2015."

ANNOTATION_TEXT = "As of Q3 2015,\nmore than 1/3 of\nprojects are missing goals"
ANNOTATION_BOLD_PHRASE = "more than 1/3"

# Value labels to show: list of (segment_index, period_index, format_str)
VALUE_LABELS = [
    (2, 6, "12%"),
    (2, 7, "15%"),
    (2, 8, "20%"),
    (2, 9, "33%"),
    (2, 10, "42%"),
]

# --- STYLE ---
GRAY_300 = "#C0C0C0"
GRAY_500 = "#999999"
GRAY_700 = "#666666"
GRAY_900 = "#333333"

# --- OUTPUT ---
FIGURE_WIDTH = 11
FIGURE_HEIGHT = 7
DPI = 150
OUTPUT_FILE = "bar_stacked.png"

# ============================================================
# CHART CODE — Modify below for advanced customization
# ============================================================

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.edgecolor": GRAY_300,
    "axes.linewidth": 0.8,
    "axes.grid": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "xtick.color": GRAY_700,
    "ytick.color": GRAY_700,
    "xtick.major.size": 0,
    "ytick.major.size": 0,
    "text.color": GRAY_900,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 11,
    "figure.dpi": DPI,
})

fig, ax = plt.subplots(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))

x = np.arange(len(periods))
bar_width = 0.65

bottom = np.zeros(len(periods))
bar_groups = []
for label, values, color in segments:
    bars = ax.bar(x, values, bottom=bottom, width=bar_width,
                  color=color, edgecolor="white", linewidth=0.5, label=label)
    bar_groups.append((bars, values, color))
    bottom += np.array(values)

for seg_idx, period_idx, label_text in VALUE_LABELS:
    seg_label, seg_values, seg_color = segments[seg_idx]
    y_bottom = sum(segments[s][1][period_idx] for s in range(seg_idx))
    y_center = y_bottom + seg_values[period_idx] / 2
    ax.text(period_idx, y_center, label_text, ha="center", va="center",
            fontsize=10, fontweight="bold", color="white")

ax.set_xticks(x)
ax.set_xticklabels(periods, fontsize=10)
ax.set_ylim(0, 105)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f"{y:.0f}%"))
ax.set_ylabel("% of total projects", fontsize=11, color=GRAY_700)

import matplotlib.patches as mpatches
legend_handles = [mpatches.Patch(color=color, label=label)
                  for label, _, color in segments]
legend = ax.legend(handles=legend_handles,
                   loc="upper left", bbox_to_anchor=(0.0, 1.04),
                   ncol=len(segments), frameon=False, fontsize=10,
                   handletextpad=0.3, columnspacing=1.5)
for text in legend.get_texts():
    text.set_color(GRAY_700)

ax.text(8.5, 60, ANNOTATION_TEXT, fontsize=12, color=GRAY_900,
        ha="center", va="top", linespacing=1.3)

fig.text(0.04, 0.97, TITLE, fontsize=16, fontweight="bold",
         color=GRAY_900, ha="left", va="top", transform=fig.transFigure)

if SOURCE:
    fig.text(0.04, 0.02, SOURCE, fontsize=8, color=GRAY_500, ha="left")

plt.tight_layout(rect=[0, 0.05, 1, 0.90])
plt.savefig(OUTPUT_FILE, dpi=DPI, bbox_inches="tight", facecolor="white")
plt.show()
print(f"Chart saved to {OUTPUT_FILE}")
