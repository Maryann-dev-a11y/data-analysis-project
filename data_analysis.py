import pandas as pd

# Step 1: Create a synthetic dataset representing sales over different regions
data = {
    'date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05'],
    'sales': [200, 220, 250, 270, 300],
    'region': ['North', 'South', 'East', 'West', 'North'],
}

# Step 2: Create a DataFrame
df = pd.DataFrame(data)

# Step 3: Save the dataset to a CSV file
df.to_csv('dataset.csv', index=False)

# Step 4: Load the dataset from the CSV file (for further analysis)
df_loaded = pd.read_csv('dataset.csv')

# Step 5: Display the first few rows of the dataset to confirm it's loaded correctly
print("First few rows of the dataset:")
print(df_loaded.head())

# Optional: Check the structure of the dataset (types and missing values)
print("\nDataset Info:")
print(df_loaded.info())

# Optional: Check for missing values
print("\nMissing Values:")
print(df_loaded.isnull().sum())
