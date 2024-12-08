import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
#from scipy.stats import zscore

plt.style.use('ggplot')
pd.set_option('display.max_columns', 20)

#load the dataset
df = pd.read_csv('/Users/hazel/Downloads/data/benin-malanville.csv')

# 1. understanding the data
print(df.shape)
#print(df.info)
#print(df.head(5)) - to see the first 5 rows of the data
#print(df.columns) 
#the list of columns
#print(df.dtypes) - to list the datatypes



