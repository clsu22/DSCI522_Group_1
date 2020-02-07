# author: Haoyu Su 
# date: 2020-01-23

"Creates eda plots for the pre-processed training data from the credit approval data.
Saves the plots as png files.

Usage: src/visualization.R --train=<train> --out_dir=<out_dir>

Options:
--train=<train>      Path (including filename) to training data (which needs to be saved as a csv file).
--out_dir=<out_dir>  Path to directory where the figures will be saved.
" -> doc

library(dplyr)
library(readr)
library(ggplot2)
library(cowplot)
library(ggridges) 
library(docopt)

opt <- docopt(doc)

main <- function(train, out_dir) {
  # Load data
  theme_set(theme_cowplot())
  
  options(repr.plot.height = 5, repr.plot.width = 8)
  
  df <- read_csv(train)
  
  data_df <- df %>% 
    mutate(Recurrence = if_else(Class == 0, "No", "Yes"))
  
  
  # Plot class against age 
  p1 <- data_df %>% 
    group_by(age_group, Recurrence) %>% 
    summarise(counts = n()) %>%
    bind_rows(tibble(age_group = c("20-29", "70-79"), 
                     Recurrence = rep("Yes", 2), 
                     counts = rep(0,2))) %>% 
    ggplot(aes(x = age_group, y = counts, fill= Recurrence)) +
    geom_bar(stat = "identity", position = "dodge") +
    labs(title = "Recurrence vs. Age", 
         y = "Number of patients", 
         x = "Age group") +
    theme(axis.text = element_text(size = 18),
          text = element_text(size = 20),
          legend.text = element_text(size = 18),
          plot.title = element_text(face = "plain"),
          legend.position="bottom")
  
  
  # Plot class against avg_tumor_size
  p2 <- data_df %>% 
    ggplot(aes(y = Recurrence, x = avgerage_tumor_size, vline_color = ..quantile..)) +
    geom_density_ridges(alpha = 0.6, scale = 1, quantile_lines = TRUE) + 
    scale_discrete_manual("vline_color",
                          values = c("blue", "red", "blue", "black"), 
                          breaks = c(1, 2),
                          labels = c("1st & 3rd quartile", "median"),
                          name = NULL) +
    labs(title = "Recurrence vs. Average tumor size", 
         y = "Recurrence", 
         x = "Average tumor size") +
    xlim(0,  55) +
    theme(axis.text = element_text(size = 18),
          text = element_text(size = 20),
          legend.text = element_text(size = 18),
          plot.title = element_text(face = "plain"),
          legend.position="bottom")
  
  try({
    dir.create(out_dir)
  })
  
  
  # Save figures
  ggsave(plot=plot_grid(p1, p2, labels = c('A', 'B'), label_size = 18, ncol = 2),
         path = out_dir, "data_analysis.png", width = 16, height = 5, dpi = 300)
}

main(opt[["--train"]], opt[["--out_dir"]])