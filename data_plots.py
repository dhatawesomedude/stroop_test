import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import seaborn as sns



def congruent_plot(sorted_df):
	mu = sorted_df.mean()
	sigma = sorted_df.std()

	fig, ax = plt.subplots()

	# plot Congruent means
	n, bins, patches = ax.hist(sorted_df['Congruent'], normed=1)

	#print(mu.Congruent)


	# add a 'best fit' line
	y = mlab.normpdf(bins, mu.Congruent, sigma.Congruent)
	ax.plot(bins, y, '--')
	ax.set_xlabel('time(s)')
	ax.set_ylabel('Probability density')
	ax.set_title('Histogram of congruent test: $\mu=$' + str(round(mu.Congruent, 2)) + ', $\sigma=$' + str(round(sigma.Congruent, 2)) + ' ')


	# Tweak spacing to prevent clipping of ylabel
	fig.tight_layout()
	plt.show()

def incongruent_plot(sorted_df):
	mu = sorted_df.mean()
	sigma = sorted_df.std()

	fig, ax = plt.subplots()

	# plot Congruent means
	n, bins, patches = ax.hist(sorted_df['Incongruent'], normed=1)

	#print(mu.Incongruent)


	# add a 'best fit' line
	y = mlab.normpdf(bins, mu.Incongruent, sigma.Incongruent)
	ax.plot(bins, y, '--')
	ax.set_xlabel('time(s)')
	ax.set_ylabel('Probability density')
	ax.set_title('Histogram of incongruent test: $\mu=$' + str(round(mu.Incongruent, 2)) + ', $\sigma=$' + str(round(sigma.Incongruent, 2)) + ' ')


	# Tweak spacing to prevent clipping of ylabel
	fig.tight_layout()
	plt.show()

def box_plot(data):
	labels = ['congruent', 'Incongruent']
	fig, ax = plt.subplots()
	ax.boxplot(data, 0, 'gD', labels=labels, meanline=True, showfliers=True, showcaps=True)
	ax.set_title('Box plot showing distribution and outliers')


	plt.show()
