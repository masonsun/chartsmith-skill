"""
Chartsmith — Slope Chart
Inspired by: Knaflic "Employee feedback over time"

Shows change between two time periods with highlighted trends.
"""

# ============================================================
# CONFIGURATION — Edit these variables to customize your chart
# ============================================================

# --- DATA ---
# Each item: (category, start_value, end_value)
items = [
    ("Survey category | Percent favorable", 91, 96),
    ("Peers", 85, 85),
    ("Culture", 80, 80),
    ("Work environment", 76, 75),
    ("Leadership", 59, 62),
    ("Career development", 49, 45),
    ("Rewards & recognition", 41, 42),
    ("Perf management", 33, 33),
]

PERIOD_START = "2014"
PERIOD_END = "2015"

# Items to highlight (must match category names exactly)
HIGHLIGHT_ITEMS = {
    "Career development": {"color": "#C75B12", "note": ""},
    "Perf management": {"color": "#C75B12", "note": ""},
}

# Visual grouping: insert extra whitespace after these indices
GROUP_BREAKS_AFTER = [0, 3, 4]

# --- CONTENT ---
TITLE = "Employee feedback over time"
SUBTITLE = "Survey year"
SOURCE = ""

# --- STYLE ---
DEFAULT_LINE_COLOR = "#999999"
GRAY_500 = "#999999"
GRAY_700 = "#666666"
GRAY_900 = "#333333"

LINE_WIDTH_DEFAULT = 1.5
LINE_WIDTH_HIGHLIGHT = 2.5
DOT_SIZE_DEFAULT = 40
DOT_SIZE_HIGHLIGHT = 60

# --- OUTPUT ---
FIGURE_WIDTH = 8
FIGURE_HEIGHT = 9
DPI = 150
OUTPUT_FILE = "slope_chart.png"

# ============================================================
# CHART CODE — Modify below for advanced customization
# ============================================================

import matplotlib.pyplot as plt

plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.grid": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.spines.left": False,
    "axes.spines.bottom": False,
    "text.color": GRAY_900,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 11,
    "figure.dpi": DPI,
})

fig, ax = plt.subplots(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))

y_positions = []
current_y = 0
for i in range(len(items)):
    y_positions.append(current_y)
    current_y -= 1
    if i in GROUP_BREAKS_AFTER:
        current_y -= 0.6

x_left = 0
x_right = 1

for i, (cat, start_val, end_val) in enumerate(items):
    y = y_positions[i]
    highlight = HIGHLIGHT_ITEMS.get(cat)

    if highlight:
        color = highlight["color"]
        lw = LINE_WIDTH_HIGHLIGHT
        dot_size = DOT_SIZE_HIGHLIGHT
        text_weight = "bold"
    else:
        color = DEFAULT_LINE_COLOR
        lw = LINE_WIDTH_DEFAULT
        dot_size = DOT_SIZE_DEFAULT
        text_weight = "normal"

    ax.plot([x_left, x_right], [y, y], color=color, linewidth=lw, zorder=2)
    ax.scatter([x_left, x_right], [y, y], s=dot_size, color=color, zorder=3)

    ax.text(x_left - 0.05, y, f"{cat}  {start_val}%",
            ha="right", va="center", fontsize=10, color=color, fontweight=text_weight)
    ax.text(x_right + 0.05, y, f"{end_val}%",
            ha="left", va="center", fontsize=10, color=color, fontweight=text_weight)

ax.text(x_left, y_positions[0] + 0.8, PERIOD_START,
        ha="center", va="bottom", fontsize=11, color=GRAY_700)
ax.text(x_right, y_positions[0] + 0.8, PERIOD_END,
        ha="center", va="bottom", fontsize=11, color=GRAY_700)

ax.text((x_left + x_right) / 2, y_positions[-1] - 1.2, SUBTITLE,
        ha="center", va="top", fontsize=10, color=GRAY_700)

ax.set_xlim(-0.6, 1.6)
ax.set_ylim(y_positions[-1] - 1.5, y_positions[0] + 1.2)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

fig.suptitle(TITLE, x=0.5, y=0.97, ha="center", fontsize=16, fontweight="bold",
             color=GRAY_900)

if SOURCE:
    fig.text(0.04, 0.02, SOURCE, fontsize=8, color=GRAY_500, ha="left")

plt.tight_layout(rect=[0.25, 0.03, 0.85, 0.94])
plt.savefig(OUTPUT_FILE, dpi=DPI, bbox_inches="tight", facecolor="white")
plt.show()
print(f"Chart saved to {OUTPUT_FILE}")
