# ----------------------------------------------
# LONDON HOUSING DATASET ANALYSIS - DAY 6 PROJECT
# ----------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------------------------
# 1. Load Dataset
# -------------------------------------------------
df = pd.read_csv('london house dataset.csv')

print(df.head())
print("Total rows:", len(df))

# -------------------------------------------------
# 2. Check Null Values
# -------------------------------------------------
print("\nColumn-wise record counts:")
print(df.count())

print("\nNull value summary:")
print(df.isnull().sum())

# Heatmap for missing values
sns.heatmap(df.isnull())
plt.title("Missing Values Heatmap")
plt.show()

# -------------------------------------------------
# 3. Convert 'date' column to datetime format
# -------------------------------------------------
print("\nData types before conversion:")
print(df.dtypes)

df['date'] = pd.to_datetime(df['date'])

print("\nData types after conversion:")
print(df.dtypes)

# -------------------------------------------------
# 4. Add 'Year' column (Extracted from date)
# -------------------------------------------------
df['Year'] = df['date'].dt.year

# -------------------------------------------------
# 5. Add 'month' column as the 2nd column
# -------------------------------------------------
df.insert(2, 'month', df.date.dt.month)

print("\nDataframe with Year & Month columns:")
print(df.head())

# -------------------------------------------------
# 6. Remove Year and Month columns (optional)
# -------------------------------------------------
# df.drop(['month', 'Year'], axis=1, inplace=True)

# -------------------------------------------------
# 7. Filter records where number of crimes = 0
# -------------------------------------------------
crime_zero_df = df[df.no_of_crimes == 0]
print("\nRecords where No. of Crimes = 0:")
print(crime_zero_df)

print("\nTotal records with 0 crimes:", len(crime_zero_df))

# -------------------------------------------------
# 8. Max & Min Average Price per year in England
# -------------------------------------------------
df_england = df[df.area == 'england']

max_price_sum = df_england.groupby('Year').average_price.max().sum()
min_price_sum = df_england.groupby('Year').average_price.min().sum()
mean_price_sum = df_england.groupby('Year').average_price.mean().sum()

print("\nSum of max average prices per year (England):", max_price_sum)
print("Sum of min average prices per year (England):", min_price_sum)
print("Sum of mean average prices per year (England):", mean_price_sum)

# -------------------------------------------------
# 9. Maximum & Minimum number of crimes per area
# -------------------------------------------------
crime_max = df.groupby('area').no_of_crimes.max()
crime_sorted = crime_max.sort_values()

print("\nMaximum no_of_crimes per area:")
print(crime_max)

print("\nAreas sorted by crime count:")
print(crime_sorted)

# -------------------------------------------------
# 10. Count records per area where average price < 100000
# -------------------------------------------------
price_below_100k = df[df.average_price < 100000].area.value_counts()

print("\nRecord count per area where average price < 100000:")
print(price_below_100k)

# -----------------------------
# END OF PROJECT
# -----------------------------
