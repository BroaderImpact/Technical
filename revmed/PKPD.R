# Pharmacokinetic Modeling
# load necessary packages
library(dplyr)
library(nlme)
library(plotly)

# read in data
data <- read.csv("drug_trial_data.csv")

# define model equation
PK_model <- function(T, A, k, V) {
  A * exp(-k*T) / V
}

# fit PK model
PK_fit <- nlsList(Cp ~ PK_model(T, A, k, V),
                  data = data,
                  start = list(A = 100, k = 0.1, V = 10))

# extract PK parameters
PK_params <- summary(PK_fit)$parameters

# plot PK curve
plot_data <- data %>%
  mutate(PK_pred = predict(PK_fit)) %>%
  select(T, Cp, PK_pred)

plot_ly(plot_data, x = ~T) %>%
  add_lines(y = ~Cp, name = "Observed") %>%
  add_lines(y = ~PK_pred, name = "Predicted")

# print PK parameter estimates
PK_params

# Pharmacodynamic Modeling

# load necessary packages
library(dplyr)
library(nlme)
library(plotly)

# read in data
data <- read.csv("drug_trial_data.csv")

# define model equation
PD_model <- function(E, E0, Imax, IC50, gamma) {
  E0 + (Imax * E^gamma) / (IC50^gamma + E^gamma)
}

# fit PD model
PD_fit <- nlsList(E ~ PD_model(Cp, E0, Imax, IC50, gamma),
                  data = data,
                  start = list(E0 = 10, Imax = 100, IC50 = 50, gamma = 1))

# extract PD parameters
PD_params <- summary(PD_fit)$parameters

# plot PD curve
plot_data <- data %>%
  mutate(PD_pred = predict(PD_fit)) %>%
  select(Cp, E, PD_pred)

plot_ly(plot_data, x = ~Cp) %>%
  add_lines(y = ~E, name = "Observed") %>%
  add_lines(y = ~PD_pred, name = "Predicted")

# print PD parameter estimates
PD_params
