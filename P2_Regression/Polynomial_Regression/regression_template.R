# Regression Template

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$DependentVariable, SplitRatio = 0.8)
# training_set = subset(dataset, split == TRUE)
# test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)

# Fitting Polynomial Regression to the dataset
# Create your regressor here

# Visualising the Polynomial Regression Results
# install.packages(ggplot2)
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), color = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)), color = 'blue') +
  ggtitle('Truth or Bluff (Polynomial Regression Results)') +
  xlab('Position Level') +
  ylab('Salary')

# Predicting a new result with Polynomial Regression
y_pred = predict(poly_reg, data.frame(Level = 6.5, 
                                      Level2 = 6.5^2,
                                      Level3 = 6.5^3,
                                      Level4 = 6.5^4))

# Visualising the Polynomial Regression Results (for higher resolution)
# install.packages(ggplot2)
library(ggplot2)
x_grid$Level = seq(min(dataset$Level), max(dataset$Level), 0.1)
x_grid$Level2 = x_grid$Level^2
x_grid$Level3 = x_grid$Level^3
x_grid$Level4 = x_grid$Level^4
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), color = 'red') +
  geom_line(aes(x = x_grid$Level, y = predict(poly_reg, newdata = x_grid)), color = 'blue') +
  ggtitle('Truth or Bluff (Polynomial Regression Results)') +
  xlab('Position Level') +
  ylab('Salary')