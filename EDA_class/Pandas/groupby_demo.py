import pandas as pd

df = pd.read_csv(
    r"C:\Users\hp\Downloads\customer1.txt",
    names=['id', 'fname', 'lname', 'age', 'prof', 'loc']
)

# Fill missing location
df['loc'] = df['loc'].fillna('india')
# print(df.isna().sum())

# # Location-wise count
# df1 = df.groupby('loc').count().sort_values(ascending=False)
# print(df1)
#
# # Profession-wise count
# df2 = df.groupby('prof').count().sort_values(ascending=False)
# print(df2)

df4 = df.groupby('prof')['age'].max()
print(df4)
print('-'*100)
df5= df.groupby('prof')['age'].min()
print(df5)
print('-'*100)
df6= df.groupby('prof')['age'].median()
print(df6)

print('-'*100)
df7= df.groupby('loc')['age'].mean().round()
print(df7)

df8 = df.groupby(['loc','prof'])['age'].count()
print(df8)
