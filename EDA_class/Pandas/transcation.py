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
print("-"*100)
#How many transactions were made using each payment method?
df8 = df['method'].value_counts()

print(df8)
print("-"*100)
#.How many transactions happened from January to June 2011?
df9 = df.loc[df['dat'].between("2011-01-01","2011-06-30")]
print(df9.shape[0])
print("-"*100)
#Find the total payment amount for each category.
df10 = df.groupby('category')['pay_amount'].sum()
print(df10)
print("-"*100)
#average payment amount per category
df12 = df.groupby('category')['pay_amount'].mean()
print(df12)
print("-"*100)

#total payment from cash and credit method
df13 =df.groupby ('method',as_index=False)['pay_amount'].sum()
print(df13)
print("-"*100)

#find the total payment for indoor game category
df14 = df.loc[df['category']=="Indoor Games"]
print(df14['pay_amount'].sum())
print("-"*100)

#transaction each state
df15 = df.groupby('state')['oid'].count().sort_values(ascending=True)
print(df15)
print("-"*100)

#all categories where total payment exceeds 300
# df16 = df.groupby('category',as_index=False)['pay_amount'].sum()
# df16_jo = df16.loc[df16['pay_amount']>=5000]
# # print(df16[df16>300])
# print(df16_jo)
df16 = (
    df.groupby('category',as_index= False)
    ['pay_amount'].sum()
    .loc[lambda x:x['pay_amount']>5000]
    .sort_values(by='pay_amount')
)
print(df16)
print("-"*100)
#highest and lowest payment in each category
df17 = (
    df.groupby('category')['pay_amount'].agg([max,min]),

)
print(df17)
print("-"*100)

#distinct product categories available in datasets
print(df['product'].unique())
print(df['product'].nunique())
print("-"*100)

#Find the total payment received per payment method per state.
df19 = df.groupby(['state','method'],as_index=False)['pay_amount'].sum()
print(df19)

#Find the most expensive transaction made in each state.
df20 =df.groupby('state',as_index=False)['pay_amount'].max()
print(df20)

#.Show the number of distinct cities where transactions took place.
