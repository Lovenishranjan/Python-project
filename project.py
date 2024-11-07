import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data using pandas
data = pd.read_csv('Desktop\py project\data.csv')

# Display total statistics
total_cases = data['New_Cases'].sum()
total_deaths = data['Deaths'].sum()
total_recoveries = data['Recoveries'].sum()
print(f"Total Cases: {total_cases}")
print(f"Total Deaths: {total_deaths}")
print(f"Total Recoveries: {total_recoveries}")

# Calculate daily changes
data['Daily_Cases'] = data['New_Cases'].diff().fillna(data['New_Cases'])
data['Daily_Deaths'] = data['Deaths'].diff().fillna(data['Deaths'])

# Plot 1: New Cases Over Time
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['New_Cases'], marker='o', color='blue', label='New Cases')
plt.title('COVID-19 New Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Number of New Cases')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Plot 2: Total Cases by Region
unique_regions = data['Region'].unique()
total_cases_per_region = data.groupby('Region')['New_Cases'].sum()

plt.figure(figsize=(10, 6))
plt.bar(total_cases_per_region.index, total_cases_per_region.values, color='purple')
plt.title('Total COVID-19 Cases by Region')
plt.xlabel('Region')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 3: Vaccination Distribution
total_vaccinated = data['Vaccinated'].sum()
total_unvaccinated = data['Population'].sum() - total_vaccinated

labels = ['Vaccinated', 'Unvaccinated']
sizes = [total_vaccinated, total_unvaccinated]
colors = ['#4CAF50', '#FFC107']

plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Vaccination Distribution')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.show()

# Plot 4: Daily Change in New Cases
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Daily_Cases'], marker='o', color='orange', label='Daily New Cases')
plt.plot(data['Date'], data['Daily_Deaths'], marker='x', color='red', label='Daily Deaths')
plt.title('Daily Changes in COVID-19 Cases and Deaths')
plt.xlabel('Date')
plt.ylabel('Number of Cases / Deaths')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Plot 5: Total Cases, Deaths, and Recoveries Over Time
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['New_Cases'].cumsum(), marker='o', color='blue', label='Total Cases')
plt.plot(data['Date'], data['Deaths'].cumsum(), marker='x', color='red', label='Total Deaths')
plt.plot(data['Date'], data['Recoveries'].cumsum(), marker='s', color='green', label='Total Recoveries')
plt.title('Total COVID-19 Cases, Deaths, and Recoveries Over Time')
plt.xlabel('Date')
plt.ylabel('Cumulative Numbers')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
