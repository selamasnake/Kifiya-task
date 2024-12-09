import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
from scipy.stats import zscore

plt.style.use('ggplot')
pd.set_option('display.max_columns', 20)

#load the dataset
df = pd.read_csv('/Users/hazel/Downloads/data/benin-malanville.csv')

# 1. understanding the data
#print(df.shape)
#print(df.info)
#print(df.head(5)) - to see the first 5 rows of the data
#print(df.columns) 
#the list of columns
#print(df.dtypes) - to list the datatypes

### 2. Data Preparation
#check for datatypes
#print(df.dtypes)

#change to appropriate datatypes
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
# print(df.dtypes)

#check for Missing Values
#print(df.isnull().sum())

#there is a missing value on one column so we'll drop it and update the dataset
df = df.drop(['Comments'], axis= 1).copy()

#check for duplicates
#print(df.duplicated().sum())
# there are no duplicates 

#check for incorrect entries and update to zero
# df['GHI'] = df['GHI'].apply(lambda x: max(x, 0))
# df['DNI'] = df['DNI'].apply(lambda x: max(x, 0))
# df['DHI'] = df['DHI'].apply(lambda x: max(x, 0))

#drop rows with negative values
df = df[df['GHI'] >= 0]
df = df[df['DNI'] >= 0]
df = df[df['DHI'] >= 0]

# print(df.shape)

#Create statistical Analysis
#print(df.describe)


#check for outliers using z-score
#df['DNI_z_score'] = zscore(df['DHI'])


#create a histogram to check frequency
#GHI, DNI, DHI histograms
#sns.histplot(df['GHI'], bins=50, color='blue', label='GHI', kde=True)
#sns.histplot(df['DNI'], bins=30, color='red', label='Direct Normal Irradiance', kde=True)
#sns.histplot(df['DHI'], bins=30, color='green', label='Diffuse Horizontal Irradiance', kde=True)

# plt.title('Comparison of DHI, GHI, DNI')
# plt.xlabel('Irradiance (W/m²)')
# plt.ylabel('Frequency')
# plt.legend()
# plt.show()


#TimeSeries Analysis
#Resample by Timestamp to Hour
# df.set_index('Timestamp', inplace=True)
# print("before sample", df.head())
# hourly_data = df.resample('h').mean()


# #DHI, DNI, GHI by hour
# plt.figure(figsize=(10, 6))

# sns.lineplot(data=hourly_data, x=hourly_data.index, y='GHI', label='GHI (W/m²)', color='darkred')
# sns.lineplot(data=hourly_data, x=hourly_data.index, y='DNI', label='DNI (W/m²)', color='orange')
# sns.lineplot(data=hourly_data, x=hourly_data.index, y='DHI', label='DHI (W/m²)', color='teal')

# # Customize the plot
# plt.title('Hourly Resampled Data for GHI, DNI, DHI')
# plt.xlabel('Time')
# plt.ylabel('Values')
# plt.legend()
# #plt.xticks(rotation=45)
# plt.grid(True)
# plt.tight_layout()

# # Show the plot
# plt.show()

# #Tamb
# sns.lineplot(data=hourly_data, x=hourly_data.index, y='Tamb', label='Tamb (°C)', color='orange')
# plt.title('Hourly Resampled Data Tamb')
# plt.xlabel('Time')
# plt.ylabel('Values')
# plt.legend()
# plt.show()


#Monthly Analysis

# monthly_data = df.resample('M').mean()
# #print(hourly_data.head())

# plt.figure(figsize=(12, 6))

# sns.lineplot(data=monthly_data, x=monthly_data.index, y='GHI', label='GHI (W/m²)', color='teal')
# sns.lineplot(data=monthly_data, x=monthly_data.index, y='DNI', label='DNI (W/m²)', color='blue')
# sns.lineplot(data=monthly_data, x=monthly_data.index, y='DHI', label='DHI (W/m²)', color='yellow')

# plt.title('Monthly Resampled Data for GHI, DNI, DHI')
# plt.xlabel('Time')
# plt.ylabel('Values')
# plt.legend()
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.tight_layout()

# plt.show()


#Tamb over the months
# sns.lineplot(data=monthly_data, x=monthly_data.index, y='Tamb', label='Tamb (°C)', color='purple')
# plt.title('Monthly Resampled Data Tamb')
# plt.xlabel('Time')
# plt.ylabel('Values')
# plt.legend()
# plt.show()

####Feature Relationships
## Correlation Analysis
# sns.pairplot(df, vars=['GHI', 'DHI', 'DNI', 'TModA', 'TModB'])
# plt.show()

#Radiation with Wind Speed
# sns.scatterplot(data=df, x='WS', y='GHI', label='GHI (W/m²)')
# sns.scatterplot(data=df, x='WS', y='DNI', label='DNI (W/m²)')
# sns.scatterplot(data=df, x='WS', y='DHI', label='DHI (W/m²)')
# plt.show()

# #Wsgust
# sns.scatterplot(data=df, x='WSgust', y='GHI', label='GHI (W/m²)')
# sns.scatterplot(data=df, x='WSgust', y='DNI', label='DNI (W/m²)')
# sns.scatterplot(data=df, x='WSgust', y='DHI', label='DHI (W/m²)')
# plt.show()

# #WD
# sns.scatterplot(data=df, x='WD', y='GHI', label='GHI (W/m²)')
# sns.scatterplot(data=df, x='WD', y='DNI', label='DNI (W/m²)')
# sns.scatterplot(data=df, x='WD', y='DHI', label='DHI (W/m²)')
# plt.show()


