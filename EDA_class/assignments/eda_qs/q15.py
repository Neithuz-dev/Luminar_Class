#15.How many transactions occurred in each state?
import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Downloads\txn_windows.csv")
print(df)

df15 = df.groupby('state')["oid"].count()
print(df15)