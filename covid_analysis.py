import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

class CovidAnalyzer:
    def __init__(self, data_path):
        """Initialize the COVID analyzer with data path"""
        self.data_path = data_path
        self.df = None
        
    def load_data(self):
        """Load and prepare COVID-19 data"""
        try:
            self.df = pd.read_csv(self.data_path)
            self.df['date'] = pd.to_datetime(self.df['date'])
            print("Data loaded successfully")
        except Exception as e:
            print(f"Error loading data: {e}")
            
    def clean_data(self, countries=None):
        """Clean and filter data for specific countries"""
        if countries:
            self.df = self.df[self.df['location'].isin(countries)]
        self.df = self.df.fillna(method='ffill')
        
    def plot_total_cases(self, countries):
        """Plot total cases for selected countries"""
        plt.figure(figsize=(12, 6))
        for country in countries:
            country_data = self.df[self.df['location'] == country]
            plt.plot(country_data['date'], country_data['total_cases'], label=country)
        
        plt.title('Total COVID-19 Cases by Country')
        plt.xlabel('Date')
        plt.ylabel('Total Cases')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
    def vaccination_analysis(self):
        """Analyze vaccination progress"""
        latest_data = self.df.groupby('location').last().reset_index()
        latest_data = latest_data.sort_values('total_vaccinations_per_hundred', ascending=False)
        
        plt.figure(figsize=(12, 6))
        sns.barplot(data=latest_data.head(10), 
                   x='location', 
                   y='total_vaccinations_per_hundred')
        plt.title('Top 10 Countries by Vaccination Rate')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    # Initialize analyzer
    analyzer = CovidAnalyzer('owid-covid-data.csv')
    
    # Load and prepare data
    analyzer.load_data()
    
    # Select countries for analysis
    countries_of_interest = ['United States', 'India', 'United Kingdom', 'Brazil', 'Kenya']
    analyzer.clean_data(countries_of_interest)
    
    # Generate plots
    analyzer.plot_total_cases(countries_of_interest)
    analyzer.vaccination_analysis()

if __name__ == "__main__":
    main()