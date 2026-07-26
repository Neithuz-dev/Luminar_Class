#Find all categories where the total payment exceeds 300.
import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Downloads\txn_windows.csv")
print(df)

df16 = (df.groupby('category',as_index= False)['pay_amount'].sum()
        .loc[lambda x:x['pay_amount']>3000]
        .sort_values(by = 'pay_amount')
)
print(df16)