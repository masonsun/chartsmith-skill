"""
Chartsmith — Horizontal Bar Chart
Inspired by: Knaflic Figure 4.9 (Top 10 design concerns)

Highlights key categories with accent color, provides right-margin annotations.
"""

# ============================================================
# CONFIGURATION — Edit these variables to customize your chart
# ============================================================

# --- DATA ---
categories = [
    "Engine power is less than expected",
    "Tires make excessive noise while driving",
    "Engine makes abnormal/excessive noise",
    "Seat material concerns",
    "Excessive wind noise",
    "Hesitation or delay when shifting",
    "Bluetooth system has poor sound quality",
    "Steering system/wheel has too much play",
    "Bluetooth system is difficult to use",
    "Front seat audio/entertainment controls",
]
values = [12.9, 12.3, 11.6, 11.6, 11.0, 10.3, 10.0, 8.8, 8.6, 8.2]

# --- CONTENT ---
TITLE = "Top 10 design concerns"
SUBTITLE = "concerns per 1,000"
SOURCE = ""

HIGHLIGHT_ITEMS = [
    "Tires make excessive noise while driving",
    "Engine makes abnormal/excessive noise",
    "Excessive wind noise",
]

ANNOTATIONS = {
    "Tires make excessive noise while driving":
        "Comments indicate that noisy tire\nissues are most apparent in the rain.",
    "Engine makes abnormal/excessive noise":
        "Complaints about engine noise\ncommonly cited after the car had\nnot been driven for a while.",
    "Excessive wind noise":
        "Excessive wind noise is noted\nprimarily in freeway driving\nat high speeds.",
}

# --- STYLE ---
ACCENT_DARK = "#8B2323"
ACCENT_LIGHT = "#C4726C"
GRAY_300 = "#C0C0C0"
GRAY_500 = "#999999"
GRAY_700 = "#666666"
GRAY_900 = "#333333"

# --- OUTPUT ---
FIGURE_WIDTH = 14
FIGURE_HEIGHT = 7
DPI = 150
OUTPUT_FILE = "examples/images/bar_horizontal.png"

# ============================================================
# CHART CODE — Modify below for advanced customization
# ============================================================

import matplotlib.pyplot as plt

plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.linewidth": 0.8,
    "axes.grid": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.spines.left": False,
    "axes.spines.bottom": False,
    "xtick.major.size": 0,
    "ytick.major.size": 0,
    "text.color": GRAY_900,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 11,
    "figure.dpi": DPI,
})

fig, ax = plt.subplots(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))

n = len(categories)
categories_rev = categories[::-1]
values_rev = values[::-1]
y_positions = list(range(n))

bar_colors = [
    ACCENT_DARK if cat in HIGHLIGHT_ITEMS else GRAY_300
    for cat in categories_rev
]

ax.barh(y_positions, values_rev, color=bar_colors, height=0.65)

ax.set_yticks(y_positions)
ax.set_yticklabels(categories_rev, fontsize=10.5, color=GRAY_700)
ax.xaxis.set_visible(False)

for i, (val, cat) in enumerate(zip(values_rev, categories_rev)):
    label_color = ACCENT_DARK if cat in HIGHLIGHT_ITEMS else GRAY_500
    ax.text(val + 0.15, i, f"{val:.1f}", va="center", ha="left",
            fontsize=10.5, fontweight="bold", color=label_color)

annotation_x = max(values) * 1.3
for cat, note in ANNOTATIONS.items():
    bar_idx = categories_rev.index(cat)
    ax.text(annotation_x, bar_idx, note, va="center", ha="left",
            fontsize=9, color=ACCENT_DARK, linespacing=1.35,
            clip_on=False)

ax.set_xlim(0, max(values) * 1.1)

ax.text(0, n + 0.3, TITLE, fontsize=16, fontweight="bold",
        color=GRAY_900, ha="left", va="bottom", transform=ax.transData)
ax.text(max(values) * 0.55, n + 0.3, SUBTITLE, fontsize=11, color=GRAY_700,
        ha="left", va="bottom", transform=ax.transData)

if SOURCE:
    ax.text(0, -1.2, SOURCE, fontsize=8, color=GRAY_500, ha="left",
            transform=ax.transData)

ax.set_ylim(-0.6, n + 0.6)
fig.subplots_adjust(left=0.28, right=0.68, top=0.93, bottom=0.04)
plt.savefig(OUTPUT_FILE, dpi=DPI, bbox_inches="tight", facecolor="white")
plt.show()
print(f"Chart saved to {OUTPUT_FILE}")
