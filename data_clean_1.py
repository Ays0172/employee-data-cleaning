# Importing Necessary libraries
import pandas as pd
import numpy as np

# Loading the dataset
# "r" is used to ensure that "\" is interpreted correctly
df = pd.read_csv(r'D:\Python\Numpy\indian_employee\employee_data_sample_15000.csv', encoding='utf-8')

# Preview data
print(df.head())

# Checking datatypes
print("\nData Types:")
print(df.dtypes)

# Print column names
print("\nColumn Names:")
print(df.columns)

# Checking missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Convert numeric columns explicitly (in case of mixed types)
df['Salary (INR)'] = pd.to_numeric(df['Salary (INR)'], errors='coerce')
df['Performance Rating'] = pd.to_numeric(df['Performance Rating'], errors='coerce')
df['Experience (Years)'] = pd.to_numeric(df['Experience (Years)'], errors='coerce')
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Fill missing Salary with mean
df['Salary (INR)'] = df['Salary (INR)'].fillna(df['Salary (INR)'].mean())

# Fill missing Performance Rating with median
df['Performance Rating'] = df['Performance Rating'].fillna(df['Performance Rating'].median())

# Fill missing Experience (Years) with mean
df['Experience (Years)'] = df['Experience (Years)'].fillna(df['Experience (Years)'].mean())

# If you want to fill other missing values for numeric columns, you can do this:
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Replace all infinite values with NaN (very rare in HR data, but good for robustness)
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Remove duplicate records
df = df.drop_duplicates()

# Replace negative salaries with the mean salary (negative salary doesn't make sense)
mean_salary = df['Salary (INR)'].mean()
df['Salary (INR)'] = np.where(df['Salary (INR)'] < 0, mean_salary, df['Salary (INR)'])

# Handle outliers in Salary (removes salaries outside mean ± 3 std deviation)
salary_mean = df['Salary (INR)'].mean()
salary_std = df['Salary (INR)'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)
df = df[(df['Salary (INR)'] >= lower_bound) & (df['Salary (INR)'] <= upper_bound)]

# Saving the cleaned data file
df.to_csv(r'D:\Python\Numpy\indian_employee\cleaned_employee_data.csv', index=False)

print("\nData Cleaning Completed! Saved as: 'cleaned_employee_data.csv'")
