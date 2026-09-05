"""
Chartsmith — Annotated Line Chart
Inspired by: Knaflic "Please approve the hire of 2 FTEs" and
             "Annual giving campaign progress"

Two-series line chart with direct labeling and contextual annotation.
"""

# ============================================================
# CONFIGURATION — Edit these variables to customize your chart
# ============================================================

# --- DATA ---
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
series_primary = [155, 160, 240, 238, 185, 185, 156, 126, 104, 124, 140, 140]
series_context = [155, 160, 240, 238, 185, 185, 202, 160, 139, 149, 177, 177]

SERIES_PRIMARY_LABEL = "Processed"
SERIES_CONTEXT_LABEL = "Received"

# --- CONTENT ---
TITLE = "Please approve the hire of 2 FTEs"
SUBTITLE = "to backfill those who quit in the past year"
CHART_SUBTITLE = "Ticket volume over time"
SOURCE = ""

# Annotation block (positioned near a specific data point)
ANNOTATION_TEXT = (
    "2 employees quit in May. We nearly kept up with\n"
    "incoming volume in the following two months, but\n"
    "fell behind with the increase in Aug and haven't\n"
    "been able to catch up since."
)
ANNOTATION_X_INDEX = 5
ANNOTATION_Y_OFFSET = 50

# Data labels to show: list of (series, index) tuples
SHOW_LABELS_PRIMARY = [6, 7, 8, 9, 10]
SHOW_LABELS_CONTEXT = [6, 7, 8, 9, 10]

# --- STYLE ---
ACCENT_DARK = "#26456E"
GRAY_500 = "#999999"
GRAY_700 = "#666666"
GRAY_900 = "#333333"
GRAY_300 = "#C0C0C0"

PRIMARY_LINEWIDTH = 2.5
CONTEXT_LINEWIDTH = 1.8

# --- OUTPUT ---
FIGURE_WIDTH = 10
FIGURE_HEIGHT = 6
DPI = 150
OUTPUT_FILE = "examples/images/line_annotated.png"

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

x = range(len(months))

ax.plot(x, series_context, color=GRAY_500, linewidth=CONTEXT_LINEWIDTH,
        marker="o", markersize=4, zorder=2)
ax.plot(x, series_primary, color=ACCENT_DARK, linewidth=PRIMARY_LINEWIDTH,
        marker="o", markersize=5, zorder=3)

for i in SHOW_LABELS_PRIMARY:
    ax.text(i, series_primary[i] - 10, str(series_primary[i]),
            ha="center", va="top", fontsize=9, fontweight="bold", color=ACCENT_DARK)

for i in SHOW_LABELS_CONTEXT:
    ax.text(i, series_context[i] + 8, str(series_context[i]),
            ha="center", va="bottom", fontsize=9, color=GRAY_500)

ax.text(len(months) - 0.8, series_primary[-1], SERIES_PRIMARY_LABEL,
        va="center", ha="left", fontsize=11, fontweight="bold", color=ACCENT_DARK)
ax.text(len(months) - 0.8, series_context[-1], SERIES_CONTEXT_LABEL,
        va="center", ha="left", fontsize=11, color=GRAY_500)

ax.annotate(
    ANNOTATION_TEXT,
    xy=(ANNOTATION_X_INDEX, max(series_context[ANNOTATION_X_INDEX],
        series_primary[ANNOTATION_X_INDEX]) + 10),
    xytext=(ANNOTATION_X_INDEX + 0.5, max(series_primary) + ANNOTATION_Y_OFFSET),
    fontsize=9, color=GRAY_900, linespacing=1.5,
    arrowprops=dict(arrowstyle="-", color=GRAY_300, lw=0.8),
    va="top",
)

ax.axvline(x=4.5, color=GRAY_300, linewidth=0.8, linestyle="-")

ax.set_xticks(x)
month_labels = months.copy()
month_labels[0] = f"{months[0]}\n2014"
ax.set_xticklabels(month_labels)

ax.set_ylabel("Number of tickets", fontsize=11, color=GRAY_700)
ax.set_ylim(0, 310)
ax.yaxis.set_major_locator(plt.MultipleLocator(50))
ax.yaxis.grid(True, color="#EEEEEE", linewidth=0.4)
ax.set_axisbelow(True)

fig.text(0.04, 0.97, TITLE, fontsize=18, fontweight="bold",
         color=GRAY_900, ha="left", va="top", transform=fig.transFigure)
fig.text(0.04, 0.91, SUBTITLE, fontsize=12, color=GRAY_700,
         ha="left", va="top", transform=fig.transFigure)
ax.set_title(CHART_SUBTITLE, loc="left", fontsize=12, color=GRAY_700, pad=12)

if SOURCE:
    fig.text(0.04, 0.02, SOURCE, fontsize=8, color=GRAY_500, ha="left")

plt.tight_layout(rect=[0, 0.03, 0.92, 0.86])
plt.savefig(OUTPUT_FILE, dpi=DPI, bbox_inches="tight", facecolor="white")
plt.show()
print(f"Chart saved to {OUTPUT_FILE}")
