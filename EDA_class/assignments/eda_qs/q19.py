#19.Find the total payment received per payment method per state
import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Downloads\txn_windows.csv")
# print(df)

df19 = df.groupby(["state",'method'],as_index= False)['pay_amount'].sum()
print(df19)