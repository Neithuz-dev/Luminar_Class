#25.Find the total payment amount made by each customer (cuid).
import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Downloads\txn_windows.csv")
# print(df)

df25 = df.groupby("cuid",as_index= False)['pay_amount'].sum()
print(df25)
