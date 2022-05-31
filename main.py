# Importing libraries
import pandas as pd

# Read csv file into a pandas dataframe
df = pd.read_csv("property data.csv")

# Take a look at the first few rows
print("Real CSV Data: \n", df.head(), 'asd', df.columns.to_list())

# Making a list of missing value types
missing_values = ["n/a", "na", "--", " ", ""]
df = pd.read_csv("property data.csv", na_values=missing_values)

all_columns = df.columns.to_list()

df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)
