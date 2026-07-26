#20.Find the most expensive transaction made in each state.
import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Downloads\txn_windows.csv")
# print(df)

df20 = df.groupby('state',as_index= False)['pay_amount'].max()
print(df20)