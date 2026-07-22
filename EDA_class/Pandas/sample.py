import pandas as pd
df = pd.read_csv(r"C:\Users\hp\Downloads\sample4.txt",sep=',',header = None)
# print(df)
# print(df.columns)
# print(df.head(5))
# print(df.tail(4))
# print(df.ndim)
df.columns =["id","fname","lname","age","phone_no","location"]
print(df)

em_df1= df[["fname","lname","age","phone_no"]]
print(em_df1)

print("-"*100)
print((df.describe(include = "all")))

