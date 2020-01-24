# author: Haoyu Su 
# date: 2020-01-23

"Creates eda plots for the pre-processed training data from the credit approval data.
Saves the plots as png files.
Usage: src/visualizations.R --train=<train> --out_dir=<out_dir>
Options:
--train=<train>      Path (including filename) to training data (which needs to be saved as a csv file).
--out_dir=<out_dir> Path to directory where the figures will be saved.
" -> doc

library(docopt)
library(tidyverse)
library(ggplot2)

opt <- docopt(doc)

main <- function(train, out_dir) {
  # load data
  df <- read_csv(train)

  # Plot class against age 
  p1 <- df %>% 
    group_by(age, Class) %>% 
    summarise(counts = n()) %>%
    bind_rows(tibble("age"= c("20-29","70-79"), "Class" = rep("recurrence-events",2), "counts"=rep(0,2))) %>%
    ggplot(aes(x = age, y = counts, fill= Class)) +
    geom_bar(stat = "identity", position = "dodge") +
    theme_bw() +
    labs(title = "Recurrence vs. age", y = "Number of patients", x = "age")
    
  
  # Plot class against avg_tumor_size
  p2 <- ggplot(df, aes(x = avg_tumor_size, ..count.., fill = Class)) +
    geom_histogram(bins = 10, alpha = 0.5, position = "identity") + 
    theme_bw() +
    labs(title = "Recurrence vs. average tumor size", y = "Number of patients", x = "average tumor size")
  
  # Save figures
  ggsave(plot=p1, path = out_dir, "age_class.png", width = 8, height = 6, dpi = 300)
  ggsave(plot=p2, path = out_dir, "tumor-size_class.png", width = 8, height = 6, dpi = 300)
}

main(opt[["--train"]], opt[["--out_dir"]])
