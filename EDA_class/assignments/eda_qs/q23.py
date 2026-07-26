#23.Show transactions that do not belong to the “Exercise & Fitness” category.
import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Downloads\txn_windows.csv")
# print(df)

df23 = df.loc[df['category']!="Exercise & Fitness"]
print(df23)