"""
Chartsmith — Waterfall Chart
Inspired by: Knaflic "2014 Headcount math"

Shows sequential gains and losses with connectors and direct value labels.
"""

# ============================================================
# CONFIGURATION — Edit these variables to customize your chart
# ============================================================

# --- DATA ---
# Each step: (label, value, type)
# type: "start", "increase", "decrease", or "end"
steps = [
    ("1/1/2014\nBeginning HC", 100, "start"),
    ("Hires", 30, "increase"),
    ("Transfers In", 8, "increase"),
    ("Transfers Out", -12, "decrease"),
    ("Exits", -10, "decrease"),
    ("12/31/2014\nEnding HC", 116, "end"),
]

# --- CONTENT ---
TITLE = "2014 Headcount math"
SUBTITLE = (
    "Though more employees transferred out of the team than transferred in,\n"
    "aggressive hiring means overall headcount (HC) increased 16% over the course of the year."
)
SOURCE = ""

# Section grouping labels (optional)
SECTION_LABELS = {
    (1, 2): "Additions",
    (3, 4): "Deductions",
}

# --- STYLE ---
ACCENT_DARK = "#2B5C8A"
ACCENT_LIGHT = "#8FABBE"
INCREASE_COLOR = "#8FABBE"
DECREASE_COLOR = "#8B2323"
START_END_COLOR = "#2B5C8A"
GRAY_300 = "#C0C0C0"
GRAY_500 = "#999999"
GRAY_700 = "#666666"
GRAY_900 = "#333333"

# --- OUTPUT ---
FIGURE_WIDTH = 10
FIGURE_HEIGHT = 6
DPI = 150
OUTPUT_FILE = "examples/images/waterfall.png"

# ============================================================
# CHART CODE — Modify below for advanced customization
# ============================================================

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.edgecolor": GRAY_300,
    "axes.linewidth": 0.8,
    "axes.grid": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.spines.left": False,
    "axes.spines.bottom": True,
    "axes.axisbelow": True,
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

n = len(steps)
bar_width = 0.5
x_positions = range(n)

running = 0
bottoms = []
heights = []
colors = []

for label, value, step_type in steps:
    if step_type == "start":
        bottoms.append(0)
        heights.append(value)
        colors.append(START_END_COLOR)
        running = value
    elif step_type == "end":
        bottoms.append(0)
        heights.append(value)
        colors.append(START_END_COLOR)
    elif step_type == "increase":
        bottoms.append(running)
        heights.append(value)
        colors.append(INCREASE_COLOR)
        running += value
    elif step_type == "decrease":
        running += value
        bottoms.append(running)
        heights.append(abs(value))
        colors.append(DECREASE_COLOR)

bars = ax.bar(x_positions, heights, bottom=bottoms, width=bar_width,
              color=colors, edgecolor="white", linewidth=0.5)

for i in range(n - 1):
    top_current = bottoms[i] + heights[i]
    ax.plot([i + bar_width / 2, i + 1 - bar_width / 2],
            [top_current, top_current],
            color=GRAY_300, linewidth=0.8, linestyle="--", zorder=1)

for i, (label, value, step_type) in enumerate(steps):
    if step_type in ("start", "end"):
        display = str(value)
        y_pos = heights[i] / 2
        ax.text(i, y_pos, display, ha="center", va="center",
                fontsize=12, fontweight="bold", color="white")
    elif step_type == "increase":
        display = f"+{value}"
        y_pos = bottoms[i] + heights[i] + 3
        ax.text(i, y_pos, display, ha="center", va="bottom",
                fontsize=11, fontweight="bold", color=INCREASE_COLOR)
    elif step_type == "decrease":
        display = f"{value}"
        y_pos = bottoms[i] + heights[i] + 3
        ax.text(i, y_pos, display, ha="center", va="bottom",
                fontsize=11, fontweight="bold", color=DECREASE_COLOR)

labels = [s[0] for s in steps]
ax.set_xticks(x_positions)
ax.set_xticklabels(labels, fontsize=10, color=GRAY_700, ha="center", linespacing=1.3)
ax.yaxis.set_visible(False)

for (start_idx, end_idx), section_label in SECTION_LABELS.items():
    mid_x = (start_idx + end_idx) / 2
    ax.text(mid_x, -18, section_label, ha="center", va="top",
            fontsize=10, fontweight="bold", color=GRAY_700)

fig.text(0.04, 0.95, TITLE, fontsize=16, fontweight="bold",
         color=GRAY_900, ha="left", va="top",
         transform=fig.transFigure)
fig.text(0.04, 0.90, SUBTITLE, fontsize=11, color=GRAY_700, ha="left", va="top",
         linespacing=1.2, transform=fig.transFigure)

if SOURCE:
    fig.text(0.04, 0.02, SOURCE, fontsize=8, color=GRAY_500, ha="left")

ax.set_ylim(0, max(bottoms[i] + heights[i] for i in range(n)) * 1.15)
plt.tight_layout(rect=[0, 0.05, 1, 0.82])
plt.savefig(OUTPUT_FILE, dpi=DPI, bbox_inches="tight", facecolor="white")
plt.show()
print(f"Chart saved to {OUTPUT_FILE}")
