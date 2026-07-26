#27.Display the first 5 transactions ordered by date
import  pandas as pd

df = pd.read_csv(r"C:\Users\hp\Downloads\txn_windows.csv")
# print(df)

df27 = df.sort_values("dat",ascending=True).head(5)
print(df27)
