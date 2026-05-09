#dalys

#import nessesary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#import dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

#explore
print("\n first 5 rows of the dataset ")
print(dalys_data.head(5))

print("\n dataset info")
print(dalys_data.info())

print("\n summary statistics")
print(dalys_data.describe())

#1. third and fourth columns (year and DALYs) for first 10 rows
print("\n third and fourth columns (year and DALYs) for first 10 rows")
first_10_years_dalys = dalys_data.iloc[0:10, 2:4]  # columns 2 and 3 (Year, DALYs)
print(first_10_years_dalys)

#find which year reported the maximum DALYs
afghanistan_data = dalys_data.loc[dalys_data.Entity == "Afghanistan", :]
#get first 10 rows of Afghanistan data
afghanistan_first_10 = afghanistan_data.iloc[0:10, :]
# find the row with maximum DALYs
max_dalys_row = afghanistan_first_10.loc[afghanistan_first_10['DALYs'].idxmax()]
max_dalys_year = max_dalys_row['Year']
print(f"\nIn Afghanistan, across the first 10 years of recorded DALYs, the maximum DALYs was reported in: {max_dalys_year}")
#Among the DALYs recorded in Afghanistan over the first 10 years, 1998 year had the maximum DALYs
#First year of data for Zimbabwe: 1990
#Last year of data for Zimbabwe: 2019

#2. use a Boolean to show all years for which DALYs were recorded in Zimbabwe
#create a Boolean mask for Zimbabwe
zimbabwe_mask = (dalys_data.Entity == "Zimbabwe")
#extract all Zimbabwe data
zimbabwe_data = dalys_data.loc[zimbabwe_mask, :]
# Get the years for Zimbabwe
zimbabwe_years = zimbabwe_data['Year']
print(f"First year of data for Zimbabwe: {zimbabwe_years.min()}")
print(f"Last year of data for Zimbabwe: {zimbabwe_years.max()}")
print(f"All years: {sorted(zimbabwe_years.unique())}")

#3. find countries with maximum and minimum DALYs in 2019
#filter for 2019 data
data_2019 = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]

#find max and min DALYs in 2019
max_dalys_2019_row = data_2019.loc[data_2019['DALYs'].idxmax()]
min_dalys_2019_row = data_2019.loc[data_2019['DALYs'].idxmin()]

country_max_dalys = max_dalys_2019_row['Entity']
max_dalys_value = max_dalys_2019_row['DALYs']
country_min_dalys = min_dalys_2019_row['Entity']
min_dalys_value = min_dalys_2019_row['DALYs']

print(f"Country with MAXIMUM DALYs in 2019: {country_max_dalys} ({max_dalys_value:.2f})")
print(f"Country with MINIMUM DALYs in 2019: {country_min_dalys} ({min_dalys_value:.2f})")

#Country with MAXIMUM DALYs in 2019: Lesotho (90771.64)
#Country with MINIMUM DALYs in 2019: Singapore (15045.11)


#4. plot DALYs over time for one of the two countries identified above
#choose the country 
selected_country = country_max_dalys
country_data = dalys_data.loc[dalys_data.Entity == selected_country, :]

#create the plot
plt.figure(figsize=(10, 6), dpi=150)
plt.plot(country_data['Year'], country_data['DALYs'], 'b-', linewidth=1.5, marker='o', markersize=3)
plt.xlabel('Year')
plt.ylabel('DALYs (Disability-Adjusted Life Years per 100,000)')
plt.title(f'DALYs Over Time for {selected_country}')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)

#save the plot
plt.savefig("dalys_trend.png")
plt.show()

#5. Question: What was the distribution of DALYs across all countries in 2019?

#plot a histogram of DALYs distribution in 2019
plt.figure(figsize=(10, 6), dpi=150)
plt.hist(data_2019['DALYs'], bins=30, edgecolor='black', alpha=0.7, color='steelblue')
plt.xlabel('DALYs (per 100,000)')
plt.ylabel('Number of Countries')
plt.title('Distribution of DALYs Across All Countries in 2019')
plt.grid(True, alpha=0.3)
plt.savefig("dalys_distribution_2019.png")
plt.show()

#calculate summary statistics for 2019 DALYs
print("\n=== 2019 DALYs Distribution Summary Statistics ===")
print(f"Mean DALYs: {data_2019['DALYs'].mean():.2f}")
print(f"Median DALYs: {data_2019['DALYs'].median():.2f}")
print(f"Standard Deviation: {data_2019['DALYs'].std():.2f}")
print(f"25th percentile: {data_2019['DALYs'].quantile(0.25):.2f}")
print(f"75th percentile: {data_2019['DALYs'].quantile(0.75):.2f}")

