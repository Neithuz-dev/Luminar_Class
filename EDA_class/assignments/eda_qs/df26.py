#26.Find which state has the highest total sales amount.
import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Downloads\txn_windows.csv")
# print(df)

df26 =(df.groupby("state",as_index=False)["pay_amount"]
       .sum()
       .sort_values("pay_amount",ascending=False))
print(df26.head(1))
