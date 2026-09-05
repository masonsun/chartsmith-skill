# Chartsmith — Sample Output (ggplot2)
# Generated from: examples/sample_data.csv
# User request: "Visualize this CSV — show how revenue compares to our targets"

# ============================================================
# CONFIGURATION — Edit these variables to customize your chart
# ============================================================

# --- DATA ---
DATA_FILE  <- "examples/sample_data.csv"
X_COLUMN   <- "month"
Y_PRIMARY  <- "revenue"
Y_CONTEXT  <- "target"

# --- CONTENT ---
TITLE    <- "Revenue exceeded targets every month since June"
SUBTITLE <- "Monthly revenue vs. target, Jan–Dec 2024 (USD)"
SOURCE   <- ""
ANNOTATION_TEXT  <- "Sustained outperformance\nbegan after the Q2\npricing restructure."
ANNOTATION_MONTH <- "Jun"

PRIMARY_LABEL <- "Revenue"
CONTEXT_LABEL <- "Target"

# --- STYLE ---
ACCENT_DARK  <- "#2B5C8A"
ACCENT_LIGHT <- "#8FABBE"
GRAY_300     <- "#C0C0C0"
GRAY_500     <- "#999999"
GRAY_700     <- "#666666"
GRAY_900     <- "#333333"

# --- OUTPUT ---
FIGURE_WIDTH  <- 11
FIGURE_HEIGHT <- 6
DPI <- 150
OUTPUT_FILE <- "examples/images/sample_output_r.png"

# ============================================================
# CHART CODE — Modify below for advanced customization
# ============================================================

library(ggplot2)
library(scales)

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
      panel.grid.major.y = element_line(color = "#EEEEEE", linewidth = 0.4),
      panel.grid.minor = element_blank(),
      legend.position = "none",
      plot.margin = margin(20, 60, 20, 20),
      plot.title.position = "plot",
      plot.caption.position = "plot"
    )
}

df <- read.csv(DATA_FILE)
df$idx <- seq_len(nrow(df))

ann_idx <- which(df[[X_COLUMN]] == ANNOTATION_MONTH)

p <- ggplot(df, aes(x = idx)) +
  geom_line(aes(y = .data[[Y_CONTEXT]]),
            color = GRAY_300, linewidth = 0.8, linetype = "dashed") +
  geom_line(aes(y = .data[[Y_PRIMARY]]),
            color = ACCENT_DARK, linewidth = 1.2) +
  geom_point(aes(y = .data[[Y_PRIMARY]]),
             color = ACCENT_DARK, size = 2.5) +
  annotate("text", x = 1, y = df[[Y_PRIMARY]][1] + 7000,
           label = paste0("$", round(df[[Y_PRIMARY]][1] / 1000), "K"),
           size = 3.5, fontface = "bold", color = ACCENT_DARK) +
  annotate("text", x = nrow(df), y = df[[Y_PRIMARY]][nrow(df)] + 7000,
           label = paste0("$", round(df[[Y_PRIMARY]][nrow(df)] / 1000), "K"),
           size = 3.5, fontface = "bold", color = ACCENT_DARK) +
  annotate("text", x = nrow(df) + 0.3, y = df[[Y_PRIMARY]][nrow(df)],
           label = PRIMARY_LABEL, hjust = 0, size = 4, fontface = "bold",
           color = ACCENT_DARK) +
  annotate("text", x = nrow(df) + 0.3, y = df[[Y_CONTEXT]][nrow(df)],
           label = CONTEXT_LABEL, hjust = 0, size = 4, color = GRAY_500) +
  annotate("text", x = ann_idx - 2, y = max(df[[Y_PRIMARY]]) + 30000,
           label = ANNOTATION_TEXT, hjust = 0, size = 3.2,
           color = GRAY_900, lineheight = 0.9) +
  annotate("segment", x = ann_idx - 0.5,
           xend = ann_idx,
           y = max(df[[Y_PRIMARY]]) + 20000,
           yend = df[[Y_PRIMARY]][ann_idx] + 3000,
           color = GRAY_300, linewidth = 0.4) +
  scale_x_continuous(breaks = seq_len(nrow(df)), labels = df[[X_COLUMN]]) +
  scale_y_continuous(labels = label_dollar(scale = 1/1000, suffix = "K"),
                     limits = c(100000, 270000)) +
  labs(title = TITLE, subtitle = SUBTITLE, x = NULL, y = NULL) +
  theme_chartsmith() +
  coord_cartesian(clip = "off")

ggsave(OUTPUT_FILE, plot = p, width = FIGURE_WIDTH, height = FIGURE_HEIGHT,
       dpi = DPI, bg = "white", units = "in")
cat(paste("Chart saved to", OUTPUT_FILE, "\n"))
