# Upper Confidence Bound

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

## Implementing Random Selection
#import random
#N = 10000
#d = 10
#ads_selected = []
#total_reward = 0
#for n in range(0, N):
#    ad = random.randrange(d)
#    ads_selected.append(ad)
#    reward = dataset.values[n, ad]
#    total_reward = total_reward + reward
#    
## Visulising the results - Histogram
#plt.hist(ads_selected)
#plt.title('Histogram of ads selections')
#plt.xlabel('Ads')
#plt.ylabel('Times Selected')
#plt.show()

# Implementing UCB
import math
N = 10000
d = 10
ads_selected = []
numbers_of_selections = np.zeros([d, 1])
sums_of_rewards = np.zeros([d, 1])
total_reward = 0
for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if (numbers_of_selections[i] > 0):
            average_reward = sums_of_rewards[i] / numbers_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    numbers_of_selections[ad] = numbers_of_selections[ad] + 1
    reward = dataset.values[n, ad]  
    sums_of_rewards[ad] = sums_of_rewards[ad] + reward
    total_reward = total_reward + reward
            
# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selection')
plt.xlabel('Ads')
plt.ylabel('Number of Times Selections')
plt.show()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        