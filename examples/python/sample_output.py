"""
Chartsmith — Sample Output
Generated from: examples/sample_data.csv
User request: "Visualize this CSV — show how revenue compares to our targets"
"""

# ============================================================
# CONFIGURATION — Edit these variables to customize your chart
# ============================================================

# --- DATA ---
DATA_FILE = "examples/sample_data.csv"
X_COLUMN = "month"
Y_PRIMARY = "revenue"
Y_CONTEXT = "target"

# --- CONTENT ---
TITLE = "Revenue exceeded targets every month since June"
SUBTITLE = "Monthly revenue vs. target, Jan–Dec 2024 (USD)"
SOURCE = ""
ANNOTATION_TEXT = "Sustained outperformance\nbegan after the Q2\npricing restructure."
ANNOTATION_MONTH = "Jun"

PRIMARY_LABEL = "Revenue"
CONTEXT_LABEL = "Target"

# --- STYLE ---
ACCENT_DARK = "#2B5C8A"
ACCENT_LIGHT = "#8FABBE"
GRAY_300 = "#C0C0C0"
GRAY_500 = "#999999"
GRAY_700 = "#666666"
GRAY_900 = "#333333"
GRAY_100 = "#E8E8E8"

# --- OUTPUT ---
FIGURE_WIDTH = 11
FIGURE_HEIGHT = 6
DPI = 150
OUTPUT_FILE = "examples/images/sample_output.png"

# ============================================================
# CHART CODE — Modify below for advanced customization
# ============================================================

import pandas as pd
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
    "figure.dpi": DPI,
})

df = pd.read_csv(DATA_FILE)

fig, ax = plt.subplots(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))

x = range(len(df))

ax.plot(x, df[Y_CONTEXT], color=GRAY_300, linewidth=1.5,
        linestyle="--", zorder=2)
ax.plot(x, df[Y_PRIMARY], color=ACCENT_DARK, linewidth=2.5,
        marker="o", markersize=5, zorder=3)

for i in [0, len(df) - 1]:
    val = df[Y_PRIMARY].iloc[i]
    ax.text(i, val + 5000, f"${val/1000:.0f}K",
            ha="center", va="bottom", fontsize=10,
            fontweight="bold", color=ACCENT_DARK)

final_val = df[Y_PRIMARY].iloc[-1]
final_target = df[Y_CONTEXT].iloc[-1]
ax.text(len(df) - 0.7, final_val, PRIMARY_LABEL,
        va="center", ha="left", fontsize=11,
        fontweight="bold", color=ACCENT_DARK)
ax.text(len(df) - 0.7, final_target, CONTEXT_LABEL,
        va="center", ha="left", fontsize=11, color=GRAY_500)

ann_idx = list(df[X_COLUMN]).index(ANNOTATION_MONTH)
ax.annotate(
    ANNOTATION_TEXT,
    xy=(ann_idx, df[Y_PRIMARY].iloc[ann_idx]),
    xytext=(ann_idx - 2.5, df[Y_PRIMARY].iloc[ann_idx] + 45000),
    fontsize=9, color=GRAY_900, linespacing=1.4,
    arrowprops=dict(arrowstyle="-", color=GRAY_300, lw=0.8),
    va="bottom", ha="left",
)

ax.set_xticks(x)
ax.set_xticklabels(df[X_COLUMN])
ax.yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda y, _: f"${y/1000:.0f}K"))
ax.yaxis.grid(True, color="#EEEEEE", linewidth=0.4)
ax.set_axisbelow(True)
ax.set_ylim(100000, 260000)

fig.text(0.06, 0.96, TITLE, fontsize=16, fontweight="bold",
         color=GRAY_900, ha="left", va="top", transform=fig.transFigure)
fig.text(0.06, 0.91, SUBTITLE, fontsize=11, color=GRAY_700,
         ha="left", va="top", transform=fig.transFigure)

if SOURCE:
    fig.text(0.06, 0.02, SOURCE, fontsize=8, color=GRAY_500, ha="left")

plt.tight_layout(rect=[0, 0.03, 0.90, 0.87])
plt.savefig(OUTPUT_FILE, dpi=DPI, bbox_inches="tight", facecolor="white")
plt.show()
print(f"Chart saved to {OUTPUT_FILE}")
