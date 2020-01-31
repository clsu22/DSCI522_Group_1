# author: Haoyu Su 
# date: 2020-01-23

"Creates eda plots for the pre-processed training data from the credit approval data.
Saves the plots as png files.

Usage: src/visualization.R --train=<train> --out_dir=<out_dir>

Options:
--train=<train>      Path (including filename) to training data (which needs to be saved as a csv file).
--out_dir=<out_dir>  Path to directory where the figures will be saved.
" -> doc

library(tidyverse)
library(cowplot)
library(ggridges) 
library(docopt)

opt <- docopt(doc)

main <- function(train, out_dir) {
  # load data
  theme_set(theme_cowplot())
  
  options(repr.plot.height = 10, repr.plot.width = 16)

  df <- read_csv(train)

  data_df <- df %>% 
    mutate(Class = if_else(Class == 0, "No recurrence", "Recurrence"))
  
  # Plot class against age 
  p1 <- data_df %>% 
    group_by(age, Class) %>% 
    summarise(counts = n()) %>%
    bind_rows(tibble(age = c("20-29", "70-79"), 
                     Class = rep("Recurrence", 2), 
                     counts = rep(0,2))) %>% 
    ggplot(aes(x = age, y = counts, fill= Class)) +
    geom_bar(stat = "identity", position = "dodge") +
    labs(title = "Recurrence vs. Age", 
         y = "Number of patients", 
         x = "Age") +
    theme(axis.text = element_text(size = 14),
          text = element_text(size = 16),
          plot.title = element_text(face = "plain"))
  
  
  # Plot class against avg_tumor_size
  p2 <- data_df %>% 
    ggplot(aes(y = Class, x = avg_tumor_size, vline_color = ..quantile..)) +
    geom_density_ridges(alpha = 0.6, scale = 1, quantile_lines = TRUE) + 
    scale_discrete_manual("vline_color",
                          values = c("blue", "red", "blue", "black"), 
                          breaks = c(1, 2),
                          labels = c("1st & 3rd quartile", "median"),
                          name = NULL) +
    labs(title = "Recurrence vs. Average tumor size", 
         y = "Class", 
         x = "Average tumor size") +
    xlim(0,  55) +
    theme(axis.text = element_text(size = 14),
          text = element_text(size = 16),
          plot.title = element_text(face = "plain"))
  
  

  # Save figures
  ggsave(plot=plot_grid(p1, p2, labels = c('A', 'B'), label_size = 12, ncol = 1),
         path = out_dir, "data_analysis.png", width = 10, height = 8, dpi = 300)
}

main(opt[["--train"]], opt[["--out_dir"]])
