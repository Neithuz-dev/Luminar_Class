#.Find average payment amount for each product category in California.
import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Downloads\txn_windows.csv")
# print(df)
df22 = (
    df.loc[df["state"]=="California"]
    .groupby("category",as_index= False)['pay_amount']
    .mean()
)
print(df22)