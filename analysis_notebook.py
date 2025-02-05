import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
try:
    df = pd.read_csv('dataset.csv')  # Replace with your actual dataset path
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("File not found. Please check the file path.")

# Display the first few rows to inspect the data
df.head()

# Explore the dataset structure
df.info()  # Check data types and missing values

# Clean the dataset: Handle missing values (you can fill or drop)
df = df.dropna()  # Drop rows with missing values (or you can use df.fillna() to fill them)

# Task 2: Basic Data Analysis

# Compute basic statistics of numerical columns
df.describe()

# Perform groupings by a categorical column (e.g., species) and compute the mean of a numerical column (e.g., sepal length)
df.groupby('region')['sales'].mean()

# Task 3: Data Visualization

# Line chart: Show trends over time (for example, time-series data if you have a 'date' column)
# Example: A time series of sales data (replace 'date' and 'sales' with your actual column names)
plt.figure(figsize=(10, 6))
df['date'] = pd.to_datetime(df['date'])  # Ensure 'date' is in datetime format
plt.plot(df['date'], df['sales'])
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.savefig('sales_trend.png')  # Save the plot as an image file
plt.close()  # Close the plot

# Bar chart: Comparison of a numerical value across categories (e.g., average sales per region)
plt.figure(figsize=(8, 6))
df.groupby('region')['sales'].mean().plot(kind='bar', color='skyblue')
plt.title('Average Sales per Region')
plt.xlabel('Region')
plt.ylabel('Average Sales')
plt.xticks(rotation=45)
plt.savefig('average_sales_per_region.png')  # Save the plot as an image file
plt.close()  # Close the plot

# Histogram: Distribution of a numerical column (e.g., sales)
plt.figure(figsize=(8, 6))
df['sales'].hist(bins=20, color='lightcoral')
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.savefig('sales_distribution.png')  # Save the plot as an image file
plt.close()  # Close the plot

# Scatter plot: Relationship between two numerical columns (e.g., sales vs. date)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='date', y='sales', data=df)
plt.title('Sales vs Date')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.savefig('sales_vs_date.png')  # Save the plot as an image file
plt.close()  # Close the plot
