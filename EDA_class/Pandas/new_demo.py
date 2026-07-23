import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Downloads\customer1.txt" ,names= ['id','fname','lname', 'age','prof','loc'])
print(df)

# print(df.isna().sum())
# df = df.fillna("india")
# print(df.isna().sum())

# df['loc'] = df['loc'].fillna('india')
# print(df.isna().sum())
#
# cs_df = df.drop_duplicates()
# print(cs_df.shape)

df2 = df.drop(['prof','id'],axis = 1)
print(df2)

df3 = df.drop([1,2],axis=0)
print(df3)

df4 = df.count()
print(df4)
