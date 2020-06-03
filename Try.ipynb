import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random

plt.style.use('fivethirtyeight')

data = pd.read_csv('insurance.csv')
#data.describe()
#data.info()
data.hist('charges')													#A single variable plot, showing how often it meets

quant_95 = data['charges'].quantile(0.95) 								#Find value that will not be exceeded in 95% cases
quant_05 = data['charges'].quantile(0.05)


def corr_func(x, y, **kwargs):											#Func calculation correlation between columns
    r = np.corrcoef(x, y)[0][1]
    ax = plt.gca()  
    ax.annotate("r = {:.2f}".format(r),
            xy=(.2, .8), xycoords=ax.transAxes,
            size = 20)

grid = sns.PairGrid(data[['charges', 'age', 'bmi', 'children']])		#Pairs plot, upper triangle has scatterplots, 
grid.map_upper(plt.scatter, color = 'red', alpha = 0.6)					#diagonal - histograms, lower - correlation
grid.map_diag(plt.hist, color = 'red', edgecolor = 'black')
grid.map_lower(corr_func)
grid.map_lower(sns.kdeplot, cmap = plt.cm.Reds)


sns.lmplot('age', 'charges', hue = 'smoker', data = data,				#Plot between two variables, shows dependence from 'smoker'
scatter_kws = {'alpha': 0.8, 's': 60}, fit_reg = False, size = 12, aspect = 1.2)
plt.xlabel("Age", size = 28), plt.ylabel('Charges', size = 28)

#plt.show()


age = int(input("Age: ")) 												#Predicting charge with input age and smoking
smoker_check = input("Smoker: ")
minbet = 1758
semi_bet = 3500
maxbet = 27700
tube = 18

if "yes" in smoker_check:
	minbet += 11500
	semi_bet += 16500
	maxbet += 11000
	semi_maxbet = 32500

	while tube < age:
		minbet += 250
		semi_bet += 250
		tube += 1
		maxbet += 235
		semi_maxbet +=310

	x = random.random()
	if x < 0.45:
		maybe_bet = random.uniform(minbet,semi_bet) 
	elif x > 0.55:
		maybe_bet = random.uniform(semi_maxbet, maxbet) 
	else: 
		maybe_bet = random.uniform(semi_bet, semi_maxbet)

else:
	while tube < age:
		minbet += 250
		semi_bet += 250
		tube += 1
		maxbet += 210	

	x = random.random()
	if x > 0.15:
		maybe_bet = random.uniform(minbet, semi_bet)
	else:
		maybe_bet = random.uniform(semi_bet, maxbet) 
print(maybe_bet)														

#Highest impact factors: age, smoker
#Quality: 64/100  -> 64%
#Result count as positive, if it was in 2000 radius from table