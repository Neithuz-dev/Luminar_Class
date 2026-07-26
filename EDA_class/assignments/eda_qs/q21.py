#.Show the number of distinct cities where transactions took place.
import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Downloads\txn_windows.csv")
# print(df)

print(df['city'].nunique())