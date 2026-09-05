# Chartsmith — Horizontal Bar Chart (ggplot2)
# Inspired by: Knaflic Figure 4.9 (Top 10 design concerns)
#
# Highlights key categories with accent color, provides right-margin annotations.

# ============================================================
# CONFIGURATION — Edit these variables to customize your chart
# ============================================================

# --- DATA ---
data <- data.frame(
  category = c(
    "Engine power is less than expected",
    "Tires make excessive noise while driving",
    "Engine makes abnormal/excessive noise",
    "Seat material concerns",
    "Excessive wind noise",
    "Hesitation or delay when shifting",
    "Bluetooth system has poor sound quality",
    "Steering system/wheel has too much play",
    "Bluetooth system is difficult to use",
    "Front seat audio/entertainment controls"
  ),
  value = c(12.9, 12.3, 11.6, 11.6, 11.0, 10.3, 10.0, 8.8, 8.6, 8.2)
)

# --- CONTENT ---
TITLE <- "Top 10 design concerns"
SUBTITLE <- "Concerns per 1,000"
SOURCE <- ""

HIGHLIGHT_ITEMS <- c(
  "Tires make excessive noise while driving",
  "Engine makes abnormal/excessive noise",
  "Excessive wind noise"
)

ANNOTATIONS <- list(
  "Tires make excessive noise while driving" =
    "Comments indicate that noisy tire\nissues are most apparent in the rain.",
  "Engine makes abnormal/excessive noise" =
    "Complaints about engine noise\ncommonly cited after the car had\nnot been driven for a while.",
  "Excessive wind noise" =
    "Excessive wind noise is noted\nprimarily in freeway driving\nat high speeds."
)

# --- STYLE ---
ACCENT_DARK  <- "#8B2323"
GRAY_300     <- "#C0C0C0"
GRAY_500     <- "#999999"
GRAY_700     <- "#666666"
GRAY_900     <- "#333333"

# --- OUTPUT ---
FIGURE_WIDTH  <- 14
FIGURE_HEIGHT <- 7
DPI <- 150
OUTPUT_FILE <- "examples/images/bar_horizontal_r.png"

# ============================================================
# CHART CODE — Modify below for advanced customization
# ============================================================

library(ggplot2)

theme_chartsmith <- function(base_size = 12) {
  theme_minimal(base_size = base_size, base_family = "Helvetica") +
    theme(
      plot.title = element_text(face = "bold", size = rel(1.3), color = GRAY_900,
                                margin = margin(b = 4)),
      plot.subtitle = element_text(size = rel(0.95), color = GRAY_700,
                                   margin = margin(b = 16)),
      plot.caption = element_text(size = rel(0.75), color = GRAY_500,
                                  hjust = 0, margin = margin(t = 12)),
      axis.title = element_text(size = rel(0.9), color = GRAY_700),
      axis.text = element_text(size = rel(0.85), color = GRAY_700),
      axis.ticks = element_blank(),
      panel.grid.major.x = element_blank(),
      panel.grid.major.y = element_blank(),
      panel.grid.minor = element_blank(),
      legend.position = "none",
      plot.margin = margin(20, 120, 20, 20),
      plot.title.position = "plot",
      plot.caption.position = "plot"
    )
}

data$category <- factor(data$category, levels = rev(data$category))
data$highlight <- ifelse(data$category %in% HIGHLIGHT_ITEMS, "yes", "no")
data$bar_color <- ifelse(data$highlight == "yes", ACCENT_DARK, GRAY_300)
data$label_color <- ifelse(data$highlight == "yes", ACCENT_DARK, GRAY_500)

p <- ggplot(data, aes(x = value, y = category)) +
  geom_col(fill = data$bar_color, width = 0.65) +
  geom_text(aes(label = sprintf("%.1f", value)),
            hjust = -0.15, size = 3.7, fontface = "bold",
            color = data$label_color) +
  scale_x_continuous(expand = expansion(mult = c(0, 0.15))) +
  labs(title = TITLE, subtitle = SUBTITLE, x = NULL, y = NULL) +
  theme_chartsmith() +
  theme(
    axis.text.x = element_blank(),
    panel.grid = element_blank()
  )

gt <- ggplotGrob(p)

ann_data <- data[data$highlight == "yes", ]
ann_x <- max(data$value) * 1.35
for (i in seq_len(nrow(ann_data))) {
  cat_name <- as.character(ann_data$category[i])
  if (cat_name %in% names(ANNOTATIONS)) {
    p <- p + annotate(
      "text", x = ann_x, y = cat_name,
      label = ANNOTATIONS[[cat_name]],
      hjust = 0, size = 3.2, color = ACCENT_DARK, lineheight = 0.9
    )
  }
}

p <- p + coord_cartesian(clip = "off")

ggsave(OUTPUT_FILE, plot = p, width = FIGURE_WIDTH, height = FIGURE_HEIGHT,
       dpi = DPI, bg = "white", units = "in")
cat(paste("Chart saved to", OUTPUT_FILE, "\n"))
