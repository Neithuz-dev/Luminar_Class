import pandas as pd
from pandas import read_csv

df = read_csv(r"C:\Users\hp\Downloads\customer1.txt" ,names= ['id','fname','lname', 'age','prof','loc'])
# print(df)
# print(df.shape)

# df1 = df.loc[: ,['fname','age','prof']].head(8)
# print(df1)

# df2  = df.loc[4:100 ,['fname','lname','prof']]
# print(df2)

# df3 = df.loc[df['loc'] == "india"].head(10)
# print(df3)

# df4 = df.loc[df['loc']=='india',['fname','age','prof']]
# print(df4)
#
# df5 = df.loc[df['age']>60,["fname",'lname','age','prof']]
# print(df5)

# df6 = df.loc[df['loc']=="uk",['fname','loc']]
# print(df6)

# df7 = df.loc[df['prof'] =="Doctor"]
# print(df7)

# df8 = df.loc[(df['loc']=="india") &( df['age']>50)]
# print(df8)

# df9 = df.loc[(df['loc'] =="uk") | (df['loc'] == "us")]
# print(df9)
# df10 = df.loc[df['loc'].isin(['uk','us','africa','china','us'])]
# print(df10)

df11 = df.loc[df['prof'].isin(['Doctor','Lawyer','Musician','Writer','Dancer'])]
print(df11)