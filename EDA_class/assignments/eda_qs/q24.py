#24.Which category has the maximum number of transactions?
import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Downloads\txn_windows.csv")
# print(df)

df24 = (df.groupby(["category"],as_index= False)["oid"]
        .count()
        .sort_values("oid",ascending=False))
print(df24.head(1))