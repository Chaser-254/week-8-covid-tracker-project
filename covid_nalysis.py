# COVID-19 Global Data Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

# Set style for visualizations
plt.style.use('seaborn')
sns.set_palette("husl")

# Load the dataset
df = pd.read_csv('owid-covid-data.csv')

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Initial data exploration
print("Dataset Overview:")
print("-----------------")
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")
print("\nColumns in dataset:")
print(df.columns.tolist())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Select countries of interest
countries_of_interest = ['United States', 'India', 'United Kingdom', 'Brazil', 'Kenya']
df_selected = df[df['location'].isin(countries_of_interest)]

# Basic cleaning
df_selected = df_selected.fillna({
    'total_cases': 0,
    'total_deaths': 0,
    'new_cases': 0,
    'new_deaths': 0
})

# Display first few rows of cleaned dataset
print("\nFirst few rows of cleaned dataset:")
print(df_selected.head())

# Create a basic line plot of total cases
plt.figure(figsize=(12, 6))
for country in countries_of_interest:
    country_data = df_selected[df_selected['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)

plt.title('COVID-19 Total Cases by Country')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()