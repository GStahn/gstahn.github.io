## ---------------------------
##
## Script name: Script_ls_cone
##
## Purpose of script: Create cone graphs 
##
## Author: Gerrit Stahn
##
## Date Created: 2025-11-24
## Last Update: 2025-11-25
##
## Copyright (c) Gerrit Stahn, 2025
## Email: gerrit.stahn@wiwi.uni-halle.de
##

## -----------------------------------------------------------------------------
## Start
## -----------------------------------------------------------------------------

### Install packages (uncomment as required) ###
# install.packages("tidyverse")

### Load add-on packages ### 
library(ggplot2)
library(dplyr)

set.seed(123)

setwd("/Users/apxww/Desktop/GitHub/myside/assets/img")

# -----------------------------
# First Graph
# -----------------------------

years <- 2025:2075
n <- length(years)

# 1) Stationary (AR(1))
mean_value <- 50000
phi <- 0.7
nfp <- numeric(n)
nfp[1] <- 50000
for (i in 2:n) {
  nfp[i] <- mean_value + phi * (nfp[i-1] - mean_value) + rnorm(1, 0, 3000)
}

# 2) Stationary with positive trend
trend <- seq(0, 60000, length.out = n)
fp <- numeric(n)
fp[1] <- 50000
for (i in 2:n) {
  fp[i] <- trend[i] + 50000 +
    phi * (fp[i-1] - (trend[i-1] + 50000)) +
    rnorm(1, 0, 2500)
}

# 3) Stationary with bigger positive trend
trend <- seq(0, 100000, length.out = n)
vfp <- numeric(n)
vfp[1] <- 50000
for (i in 2:n) {
  vfp[i] <- 1.1*trend[i] + 50000 +
    phi * (vfp[i-1] - (trend[i-1] + 50000)) +
    rnorm(1, 0, 2500)
}

### Combine ###
df <- data.frame(
  year = years,
  vfp = vfp,
  fp = fp,
  nfp = nfp
)

### Plot with ggplot2 ###
options(scipen=10000)

p <- ggplot(df) +
  geom_line(aes(x = year, y = vfp, color = "Even Better Path"), alpha = 0.5, size = 1.2, linetype= "dashed") +
  geom_line(aes(x = year, y = fp, color = "Better Path"), alpha = 0.5, size = 1.2) +
  geom_line(aes(x = year, y = nfp, color = "Less Fortunate Path"), alpha = 0.5, size = 1.2, linetype= "dotted") +
  scale_color_manual(values = rep("grey40", 3)) +
  geom_hline(yintercept = 50000) +
  labs(
    x = "Year",
    y = "Living Standard in €",
    colour =""
  ) +
  geom_polygon(
    data = data.frame(
      year = c(2025, 2075, 2075),
      value = c(50000, tail(vfp, 1), tail(nfp, 1))
    ),
    aes(x = year, y = value),
    fill = "grey60",
    alpha = 0.3,
    linetype = "dashed"
  ) +
  scale_x_continuous(limits = c(2025, 2075), breaks = seq(2025, 2075, by = 5))+ 
  scale_linetype_manual(values=c(1,4,3)) +  
  theme_minimal(base_size = 14) +
  theme(
    legend.position = "bottom",
    legend.text = element_text(size = 14)
  )+
  scale_y_continuous(
    limits = c(40000, 200000),
    breaks = seq(50000, 200000, by = 30000)
  )

p

### Save plot as PNG ###
ggsave("money_magic_plot.png", p, width = 10, height = 6, dpi = 300)

# -----------------------------
# Second Graph
# -----------------------------

# 4) New: Not so fortunate (AR(1))
trend <- seq(0, 10000, length.out = n)
nfp_up <- numeric(n)
nfp_up[1] <- 50000
for (i in 2:n) {
  nfp_up[i] <- 1.1*trend[i] + 1000 +
    phi * (fp_up[i-1] - (trend[i-1] + 1000)) +
    rnorm(1, 0, 2500)
}

# 5) New: Fortunate
trend <- seq(0, 45000, length.out = n)
fp_up <- numeric(n)
fp_up[1] <- 50000
for (i in 2:n) {
  fp_up[i] <- 1.4*trend[i] + 50000 +
    phi * (fp_up[i-1] - (trend[i-1] + 50000)) +
    rnorm(1, 0, 2500)
}

# 6) New: Very Fortunate
trend <- seq(0, 100000, length.out = n)
vfp_up <- numeric(n)
vfp_up[1] <- 50000
for (i in 2:n) {
  vfp_up[i] <- 1.12*trend[i] + 50000 +
    phi * (vfp_up[i-1] - (trend[i-1] + 50000)) +
    rnorm(1, 0, 2500)
}

### Combine ###
df <- data.frame(
  year = years,
  vfp = vfp,
  fp = fp,
  nfp = nfp,
  vfp_up = vfp_up,
  fp_up = fp_up,
  nfp_up = nfp_up
)

### Plot with ggplot2 ###
p2 <- ggplot(df) +
  geom_line(aes(x = year, y = vfp), alpha = 0.5, size = 1.2, linetype= "dashed") +
  geom_line(aes(x = year, y = fp), alpha = 0.5, size = 1.2) +
  geom_line(aes(x = year, y = nfp), alpha = 0.5, size = 1.2, linetype= "dotted") +
  geom_line(aes(x = year, y = vfp_up), alpha = 0.5, size = 1.2, linetype= "dashed", color="cadetblue1") +
  geom_line(aes(x = year, y = fp_up), alpha = 0.5, size = 1.2, color="cadetblue1") +
  geom_line(aes(x = year, y = nfp_up), alpha = 0.5, size = 1.2, linetype= "dotted", color="cadetblue1") +
  scale_color_manual(values = rep("grey40", 3)) +
  geom_hline(yintercept = 50000) +
  labs(
    x = "Year",
    y = "Living Standard in €"
  ) +
  geom_polygon(
    data = data.frame(
      year = c(2025, 2075, 2075),
      value = c(50000, tail(vfp, 1), tail(nfp, 1)),
      type = "Old Cone"
    ),
    aes(x = year, y = value, fill = type),
    alpha = 0.3,
    linetype = "dashed"
  ) +
  geom_polygon(
    data = data.frame(
      year = c(2025, 2075, 2075),
      value = c(50000, tail(vfp_up, 1), tail(nfp_up, 1)),
      type = "Improved Cone"
    ),
    aes(x = year, y = value, fill = type),
    alpha = 0.3,
    linetype = "dashed"
  )+
  scale_x_continuous(limits = c(2025, 2075), breaks = seq(2025, 2075, by = 5))+ 
  scale_linetype_manual(values=c(1,4,3)) +  
  theme_minimal(base_size = 14) +
  theme(
    legend.position = "bottom",
    legend.text = element_text(size = 14)
  )+
  scale_fill_manual(
    name = "",
    values = c(
      "Old Cone" = "grey60",
      "Improved Cone" = "cadetblue1"
    )
  )+
  scale_y_continuous(
    limits = c(40000, 200000),
    breaks = seq(50000, 200000, by = 30000)
  )

p2

### Save plot as PNG ###
ggsave("money_magic_plot2.png", p2, width = 10, height = 6, dpi = 300)

