import pandas as pd

cus_df = pd.read_csv(r"C:\Users\hp\Downloads\custom_windows.csv")
ord_df =pd.read_csv(r"C:\Users\hp\Downloads\order_windows.csv")
# print(cus_df)
# print("-"*100)
# print(ord_df)

left_join_df  = pd.merge(cus_df,ord_df,on = 'id',how="left")
print(left_join_df)

rigth_join_df = pd.merge(cus_df,ord_df,on = "id", how= "right")
print(rigth_join_df)
print("-"*100)

inner_join = pd.merge(cus_df,ord_df,on="id",how="inner")
print(inner_join)
print("-"*100)

outer_join = pd.merge(cus_df,ord_df,on="id",how="outer")
print(outer_join)
print("-"*100)

q1 = pd.merge(cus_df,ord_df,on = "id",how="inner").sort_values(by="amount",ascending=False)
q1_new = q1.groupby(["oid","dat"])["amount"].agg([min,max])
print(q1_new)

print("-"*100)
df1= (
    pd.merge(cus_df,ord_df,on="id",how="inner")
    .loc[lambda x:x["salary"]>=2000]
)
print(df1)

print("-"*100)
df2 = (
    pd.merge(cus_df,ord_df,on="id",how="inner")
    .groupby("id",as_index=False)["amount"].sum()
)
print(df2)

print("-"*100)
df3 = (
    pd.merge(cus_df,ord_df,on="id",how="inner")
    .groupby("location",as_index=False)["amount"].sum()
)
print(df3)

print("-"*100)
df4 = (
    pd.merge(cus_df,ord_df,on="id",how="inner")
    .groupby("id",as_index=False)["oid"].sum()
)
print(df4)

