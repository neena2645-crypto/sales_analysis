import sys
import subprocess

# Force install the libraries using the exact executable VS Code is running
subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "numpy", "matplotlib", "seaborn"])
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# --- 1. SIMULATE HISTORICAL TRANSACTION DATA ---
num_rows = 5000
start_date = datetime(2024, 1, 1)

data = {
    'Transaction_ID': np.arange(10000, 10000 + num_rows),
    'Date': [start_date + timedelta(days=np.random.randint(0, 365), hours=np.random.randint(9, 21)) for _ in range(num_rows)],
    'Customer_ID': np.random.randint(50001, 51500, size=num_rows), # ~1500 unique customers
    'Gender': np.random.choice(['Female', 'Male'], size=num_rows, p=[0.52, 0.48]),
    'Age': np.random.randint(18, 70, size=num_rows),
    'Product_Category': np.random.choice(['Electronics', 'Clothing', 'Beauty', 'Home & Kitchen'], size=num_rows, p=[0.30, 0.35, 0.20, 0.15]),
    'Quantity': np.random.choice([1, 2, 3, 4, 5], size=num_rows, p=[0.4, 0.3, 0.15, 0.1, 0.05]),
    'Price_Per_Unit': np.random.uniform(15.0, 500.0, size=num_rows).round(2)
}

df = pd.DataFrame(data)

# Inject intentional anomalies (Messy Data representation)
df.loc[df.sample(frac=0.01).index, 'Price_Per_Unit'] = np.nan
df.loc[df.sample(frac=0.005).index, 'Quantity'] = -1  # Returns simulated

print("--- Initial Data Structure ---")
print(df.info())

# --- 2. DATA CLEANING & ENGINEERING PIPELINE ---
# Handle structural logic anomalies
df = df[df['Quantity'] > 0] 
# Impute unit prices using the category median
df['Price_Per_Unit'] = df.groupby('Product_Category')['Price_Per_Unit'].transform(lambda x: x.fillna(x.median()))
# Calculate total derived metrics
df['Total_Amount'] = df['Quantity'] * df['Price_Per_Unit']

# Feature Extraction for Time-Series Analysis
df['Year_Month'] = df['Date'].dt.to_period('M')
df['Month_Name'] = df['Date'].dt.strftime('%B')
df['Hour'] = df['Date'].dt.hour

# Customer Demographics Feature Binning
age_bins = [0, 25, 40, 55, 100]
age_labels = ['Gen Z (18-25)', 'Millennials (26-40)', 'Gen X (41-55)', 'Boomers (56+)']
df['Age_Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

print("\n--- Data Preprocessing Complete ---")
print(f"Cleaned Row Count: {df.shape[0]}")

# --- 3. SALES PERFORMANCE METRICS ---
# Revenue Trend by Category
category_perf = df.groupby('Product_Category').agg(
    Total_Revenue=('Total_Amount', 'sum'),
    Units_Sold=('Quantity', 'sum'),
    Average_Order_Value=('Total_Amount', 'mean')
).sort_values(by='Total_Revenue', ascending=False).round(2)

print("\n--- Product Category Performance Metrics ---")
print(category_perf)

# Monthly Time Series Aggregation
monthly_sales = df.groupby('Year_Month')['Total_Amount'].sum().reset_index()
monthly_sales['Year_Month'] = monthly_sales['Year_Month'].astype(str)

# Plotting Sales Revenue Over Time
plt.figure(figsize=(12, 5))
sns.lineplot(data=monthly_sales, x='Year_Month', y='Total_Amount', marker='o', color='#1f77b4', linewidth=2.5)
plt.title('Macroscopic Monthly Revenue Tracking (2024)', fontsize=14, weight='bold')
plt.xlabel('Fiscal Timeline (Year-Month)', fontsize=11)
plt.ylabel('Gross Revenue ($)', fontsize=11)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# --- 4. BEHAVIORAL DEMOGRAPHICS DISCOVERY ---
# Cross-Tabulating Demographics and Spending
demographic_pivot = df.pivot_table(
    values='Total_Amount',
    index='Age_Group',
    columns='Gender',
    aggfunc='sum'
).round(2)

print("\n--- Spend Contribution Matrix by Age Bracket and Gender ---")
print(demographic_pivot)

# Categorical Breakdown Visualizations
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Subplot A: Revenue by Product Category broken down by Age Cohorts
sns.barplot(ax=axes[0], data=df, x='Product_Category', y='Total_Amount', hue='Age_Group', errorbar=None, palette='viridis')
axes[0].set_title('Product Category Revenue Penetration Across Age Profiles', fontsize=12, weight='bold')
axes[0].set_ylabel('Total Distribution Metric ($)')
axes[0].set_xlabel('Product Category')

# Subplot B: Correlation Matrix between Continuous Values
correlation_matrix = df[['Age', 'Quantity', 'Price_Per_Unit', 'Total_Amount']].corr()
sns.heatmap(ax=axes[1], data=correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
axes[1].set_title('Feature Interaction Correlation Matrix', fontsize=12, weight='bold')

plt.tight_layout()
plt.show()