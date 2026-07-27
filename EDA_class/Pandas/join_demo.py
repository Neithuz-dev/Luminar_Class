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