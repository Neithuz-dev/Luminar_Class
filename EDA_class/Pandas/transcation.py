import pandas as pd
df = pd.read_csv(r"C:\Users\hp\Downloads\txn_windows.csv",sep = ',')
# print(df.head(10))
# print(df.count())
# print(df.shape[0])
#
# df1 = df.groupby('city')['city'].count()
# print(df1)
#
# # print(df.dtypes)
df['dat'] = pd.to_datetime(df['dat'])
# print(df.dtypes)
print("-"*100)
# all transactions between jan 2011
df2 = df.loc[(df['dat']>="2011-01-01")& (df['dat']<="2011-01-31")]
print(df2)

df_2 = df.loc[df['dat'].between("2011-01-01","2011-01-31")]
print(df_2)
print("-"*100)
# feb transaction how many
df3 = df.loc[(df['dat']>="2011-02-01")&(df['dat']<="2011-02-28")].shape[0]
print(df3)
print("-"*100)
#july2011 with id,cat,product,state details
df4 = df.loc[
    (df['dat']>="2011-07-01")&(df['dat']<="2011-07-31") ,
    ['oid','cuid','category',"product",'state']
]

print(df4)
print(df4.shape[0])

print("-"*100)

#aug 2011 transactions
df5 = df.loc[
    (df['dat']>='2011-08-01')&(df['dat']<='2011-08-30')
]
print(df5.shape[0])
print("-"*100)

#Find how many transactions occurred in each category, and show the most frequent first.
df6 = df.groupby('category')['category'].count().sort_values(ascending=False)
print(df6)
print("-"*100)

#Show full details of transactions in the “Outdoor Recreation” category.
df7 = df.loc[df['category']=="Outdoor Recreation"]
print(df7)

#How many transactions were made using each payment method?
df8 = df['method'].value_counts()

print(df8)

#.How many transactions happened from January to June 2011?
df9 = df.loc[df['dat'].between("2011-01-01","2011-06-30")]
print(df9.shape[0])

#Find the total payment amount for each category.
df10 = df.groupby('category')['pay_amount'].sum()
print(df10)