#17.Display the highest and lowest payment made in each category.
import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Downloads\txn_windows.csv")
# print(df)

df17 = df.groupby('category')['pay_amount'].agg([min,max])
print(df17)