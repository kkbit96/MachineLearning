# Upper Confidence Bound

# Importing the dataset
dataset = read.csv('Ads_CTR_Optimisation.csv')

# Implementing UCB
d = 10
N = 1e4
ads_selected = integer()
numbers_of_selections = integer(d)
sums_of_rewards = integer(d)
total_reward = 0
for (n in 1:N) {
  max_upper_bound = 0
  ad_max_upper_bound = 0
  for (i in 1:d) {
    if (numbers_of_selections[i] > 0) {
      average_reward_i = sums_of_rewards[i] / numbers_of_selections[i]
      delta_i = sqrt(3 / 2 * log(n) / numbers_of_selections[i])
      upper_bound = average_reward_i + delta_i
    } else {
      upper_bound = 1e400
    }
    if (upper_bound > max_upper_bound) {
      max_upper_bound = upper_bound
      ad_max_upper_bound = i
    }
  }
  ads_selected = append(ads_selected, ad_max_upper_bound)
  numbers_of_selections[ad_max_upper_bound] = numbers_of_selections[ad_max_upper_bound] + 1
  reward_n = dataset[n, ad_max_upper_bound]
  sums_of_rewards[ad_max_upper_bound] = sums_of_rewards[ad_max_upper_bound] + reward_n
  total_reward = total_reward + reward_n
}

# Visualizing the results of UCB
hist(ads_selected,
     main = 'Histogram for Ads Selected',
     xlab = 'Ads',
     ylab = 'Times Selected',
     col = 'blue',
     xlim = c(1,10),
     las = 1)
