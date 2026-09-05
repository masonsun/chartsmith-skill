"""
Chartsmith — 2x2 Matrix Scatterplot
Inspired by: Knaflic Figure 5.6 (Clear visual hierarchy of information)

Scatterplot with quadrant labels, reference point, and highlighted items.
"""

# ============================================================
# CONFIGURATION — Edit these variables to customize your chart
# ============================================================

# --- DATA ---
# Each point: (name, x_value, y_value)
points = [
    ("Model A", 73, 500),
    ("Model B", 75, 1250),
    ("Model C", 76, 1050),
    ("Model D", 80, 1050),
    ("Model E", 87, 700),
    ("Model F", 79, 1000),
    ("Model G", 74, 800),
]

# Reference / benchmark point
REFERENCE_POINT = ("Prior Year Avg.\n(all models)", 70, 900)

# Items to highlight with accent color (must match point names)
HIGHLIGHT_ITEMS = ["Model B", "Model C", "Model D", "Model F"]

# --- CONTENT ---
TITLE = "Clear visual hierarchy of information"
SUBTITLE = ""
SOURCE = ""

# Axis configuration
X_LABEL = "% satisfied or highly satisfied"
Y_LABEL = "Number of Issues per 1,000"
X_HEADER = "Satisfaction"
Y_HEADER = "Things Gone\nWrong"

# Quadrant reference lines
X_THRESHOLD = 70
Y_THRESHOLD = 900

# Quadrant labels: (x_position, y_position, text)
QUADRANT_LABELS = [
    (88, 150, "High Satisfaction,\nFew Issues"),
    (88, 1350, "High Satisfaction,\nMany Issues"),
]

# Axis endpoint labels
X_LOW_LABEL = "LOW"
X_HIGH_LABEL = "HIGH"
Y_LOW_LABEL = "FEW"
Y_HIGH_LABEL = "MANY"

# Y-axis is inverted (fewer issues = better = top)
INVERT_Y = True

# --- STYLE ---
ACCENT_DARK = "#8B2323"
ACCENT_LIGHT = "#C4726C"
GRAY_300 = "#C0C0C0"
GRAY_500 = "#999999"
GRAY_700 = "#666666"
GRAY_900 = "#333333"
REFERENCE_COLOR = "#333333"

POINT_SIZE_DEFAULT = 60
POINT_SIZE_HIGHLIGHT = 80
POINT_SIZE_REFERENCE = 100

# --- OUTPUT ---
FIGURE_WIDTH = 9
FIGURE_HEIGHT = 8
DPI = 150
OUTPUT_FILE = "scatterplot_2x2.png"

# ============================================================
# CHART CODE — Modify below for advanced customization
# ============================================================

import matplotlib.pyplot as plt

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

ax.axhline(y=Y_THRESHOLD, color=GRAY_900, linewidth=1, zorder=1)
ax.axvline(x=X_THRESHOLD, color=GRAY_900, linewidth=1, zorder=1)

for name, x, y in points:
    if name in HIGHLIGHT_ITEMS:
        ax.scatter(x, y, s=POINT_SIZE_HIGHLIGHT, color=ACCENT_DARK, zorder=3)
        ax.text(x + 0.8, y + 30, name, fontsize=10, color=ACCENT_DARK, va="bottom")
    else:
        ax.scatter(x, y, s=POINT_SIZE_DEFAULT, color=GRAY_500, zorder=3)
        ax.text(x + 0.8, y + 30, name, fontsize=10, color=GRAY_500, va="bottom")

ref_name, ref_x, ref_y = REFERENCE_POINT
ax.scatter(ref_x, ref_y, s=POINT_SIZE_REFERENCE, color=REFERENCE_COLOR, zorder=4)
ax.text(ref_x - 1, ref_y, ref_name, fontsize=10, fontweight="bold",
        color=REFERENCE_COLOR, ha="right", va="center")

ax.set_xlim(58, 92)
ax.set_ylim(0, 1500)

if INVERT_Y:
    ax.invert_yaxis()

ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:.0f}%"))
ax.set_xlabel(X_LABEL, fontsize=10, color=GRAY_500, style="italic")
ax.set_ylabel(Y_LABEL, fontsize=10, color=GRAY_500)

for qx, qy, text in QUADRANT_LABELS:
    ax.text(qx, qy, text, fontsize=12, fontweight="bold", color=GRAY_700,
            ha="right", va="center", linespacing=1.3)

ax.text(0.5, 1.08, X_HEADER, transform=ax.transAxes, ha="center",
        fontsize=12, color=GRAY_900)
ax.text(0.08, 1.08, X_LOW_LABEL, transform=ax.transAxes, ha="left",
        fontsize=12, fontweight="bold", color=GRAY_900)
ax.text(0.92, 1.08, X_HIGH_LABEL, transform=ax.transAxes, ha="right",
        fontsize=12, fontweight="bold", color=GRAY_900)

ax.text(-0.14, 0.92, Y_LOW_LABEL, transform=ax.transAxes, ha="center",
        fontsize=12, fontweight="bold", color=GRAY_900)
ax.text(-0.14, 0.08, Y_HIGH_LABEL, transform=ax.transAxes, ha="center",
        fontsize=12, fontweight="bold", color=GRAY_900)
ax.text(-0.18, 0.5, Y_HEADER, transform=ax.transAxes, ha="center", va="center",
        fontsize=11, color=GRAY_900, rotation=90, linespacing=1.3)

fig.text(0.5, 0.99, TITLE, fontsize=14, fontweight="bold",
         color=GRAY_900, ha="center", va="top", transform=fig.transFigure)

if SOURCE:
    fig.text(0.04, 0.02, SOURCE, fontsize=8, color=GRAY_500, ha="left")

plt.tight_layout(rect=[0.06, 0.03, 1, 0.93])
plt.savefig(OUTPUT_FILE, dpi=DPI, bbox_inches="tight", facecolor="white")
plt.show()
print(f"Chart saved to {OUTPUT_FILE}")
