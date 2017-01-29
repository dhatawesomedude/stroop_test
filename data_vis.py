import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def cent_td_stats(sorted_df):
	mu = sorted_df.mean()
	median = sorted_df.median()

	print('mean for congruent population :', mu.Congruent)
	print('mean for incongruent population: ', mu.Incongruent)

	print('median for congruent population :', median.Congruent)
	print('median for incongruent population: ', median.Incongruent)

def variability_stats(sorted_df):
	sigma = sorted_df.std()

	print('SD for congruent population :', sigma.Congruent)
	print('SD for incongruent population: ', sigma.Incongruent)