######################
# Hypothesis testing
######################

gen_methods <- list("random","ep_random", "random+", "ep_random+")
algos <- list("lr", "xg", "rf")
metrics <- list("accuracy","f1")
stats <- list("mean", "sd")

# Read performance data
results <- list()
for (gen_method in gen_methods){
  for (algo in algos) {
    results[[gen_method]][[algo]] <- read.csv(paste("results/", gen_method, "/", algo, "_multi_test.csv", sep=''))
  }
}
results[["bg"]][["maxent"]] <- read.csv("results/presence-only/maxent_v3.csv")[,1:2]


# compute means and standard deviations
stats <- list()
for (gen_method in gen_methods){
  for (algo in algos){
    for (metric in metrics) {
      stats[[gen_method]][[algo]][[metric]][["mean"]] <- round(mean(results[[gen_method]][[algo]][[metric]]), 4)
      stats[[gen_method]][[algo]][[metric]][["sd"]] <- round(sd(results[[gen_method]][[algo]][[metric]]), 4)
    }
  }
}
for (metric in metrics){
  stats[["bg"]][["maxent"]][[metric]][["mean"]] <- round(mean(results[["bg"]][["maxent"]][[metric]]), 4)
  stats[["bg"]][["maxent"]][[metric]][["sd"]] <- round(sd(results[["bg"]][["maxent"]][[metric]]), 4)
}


################
# Omnibus test
################

tests <- list()
for (metric in metrics) {
  results_mat <- as.matrix(data.frame(random_lr=results$random$lr[[metric]],
                                      random_plus_lr=results$`random+`$lr[[metric]],
                                      ep_random_lr=results$ep_random$lr[[metric]], 
                                      ep_random_plus_lr=results$`ep_random+`$lr[[metric]],
                                      random_xgb=results$random$xg[[metric]],
                                      random_plus_xgb=results$`random+`$xg[[metric]],
                                      ep_random_xgb=results$ep_random$xg[[metric]],
                                      ep_random_plus_xgb=results$`ep_random+`$xg[[metric]],
                                      random_rf=results$random$rf[[metric]], 
                                      random_plus_rf=results$`random+`$rf[[metric]],
                                      ep_random_rf=results$ep_random$rf[[metric]],
                                      ep_random_plus_rf=results$`ep_random+`$rf[[metric]],
                                      bg_maxent=results$bg$maxent[[metric]]))
  tests[[metric]] <- friedman.test(results_mat)
}

##################
# Pairwise tests
##################
n <- 100
random_lr_label <- rep("random_lr", n)
random_xgb_label <- rep("random_xgb", n)
random_rf_label <- rep("random_rf", n)
random_plus_lr_label <- rep("random_plus_lr", n)
random_plus_xgb_label <- rep("random_plus_xgb", n)
random_plus_rf_label <- rep("random_plus_rf", n)
ep_random_lr_label <- rep("ep_random_lr", n)
ep_random_xgb_label <- rep("ep_random_xgb", n)
ep_random_rf_label <- rep("ep_random_rf", n)
ep_random_plus_lr_label <- rep("ep_random_plus_lr", n)
ep_random_plus_xgb_label <- rep("ep_random_plus_xgb", n)
ep_random_plus_rf_label <- rep("ep_random_plus_rf", n)
bg_maxent_label <- rep("bg_maxent", n)

# concatenate labels and results
gen = c(random_lr_label, random_xgb_label, random_rf_label, 
        random_plus_lr_label, random_plus_xgb_label, random_plus_rf_label,
        ep_random_lr_label, ep_random_xgb_label,ep_random_rf_label,
        ep_random_plus_lr_label, ep_random_plus_xgb_label,ep_random_plus_rf_label, bg_maxent_label)

# perform pairwise test using Holm p-value adjustment
pairwise_tests <- list()
for (metric in metrics) {
  outcome = c(random_lr=results$random$lr[[metric]], 
              random_xgb=results$random$xg[[metric]],
              random_rf=results$random$rf[[metric]], 
              random_plus_lr=results$random$lr[[metric]], 
              random_plus_xgb=results$random$xg[[metric]],
              random_plus_rf=results$random$rf[[metric]],
              ep_random_lr=results$ep_random$lr[[metric]], 
              ep_random_xgb=results$ep_random$xg[[metric]],
              ep_random_rf=results$ep_random$rf[[metric]],
              ep_random_plus_lr=results$`ep_random+`$lr[[metric]], 
              ep_random_plus_xgb=results$`ep_random+`$xg[[metric]],
              ep_random_plus_rf=results$`ep_random+`$rf[[metric]],
              bg_maxent=results$bg$maxent[[metric]])
  df <- data.frame(gen=gen, outcome=outcome)
  pairwise_tests[[metric]] <- pairwise.t.test(df$outcome, df$gen, p.adj ="holm")
}