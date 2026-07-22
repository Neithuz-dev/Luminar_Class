import pandas as pd
df = pd.read_csv(r"C:\Users\hp\Downloads\sample4.txt",sep=',',header = None)
# print(df)
# print(df.columns)
# print(df.head(5))
# print(df.tail(4))
# print(df.ndim)
# df.columns =["id","fname","lname","age","phone_no","location"]
# print(df)

# em_df1= df[["fname","lname","age","phone_no"]]
# print(em_df1)
#
# print("-"*100)
# print((df.describe(include = "all")))
#
# df2 = df.iloc[0:6]
# print(df2)

# df3 = df.iloc[4: ,-1]
# print(df3)
#
# df4 = df.iloc[:,1:4]
# print(df4)

# df5 = df.iloc[:,[1,2,5]]
# print(df5)

df6 = df.loc[ :,['fname',"age"]]
print(df6)
