import pandas as pd
from pandas import read_csv

df = read_csv(r"C:\Users\hp\Downloads\customer1.txt" ,names= ['id','fname','lname', 'age','prof','loc'])
# print(df)
# print(df.shape)

# df1 = df.loc[: ,['fname','age','prof']].head(8)
# print(df1)

# df2  = df.loc[4:100 ,['fname','lname','prof']]
# print(df2)

df3 = df.loc[df['loc'] == "india"].head(10)
print(df3)