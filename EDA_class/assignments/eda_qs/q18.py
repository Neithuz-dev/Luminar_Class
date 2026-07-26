#18.Show all distinct product categories available in the dataset.
import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Downloads\txn_windows.csv")
# print(df)

print(df['product'].unique())