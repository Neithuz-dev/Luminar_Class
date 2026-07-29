import pandas as pd

main_df = pd.read_csv(r"C:\Users\hp\Downloads\99008d4b-08f8-4b8c-917a-0d4c1b6dc906.csv")
# print(main_df)
#1
print(main_df.isna().sum())
#2
main_df= main_df.dropna(subset=["customer_name"],ignore_index=True)
print(main_df["customer_name"])
#3
main_df["order_date"] = pd.to_datetime(main_df["order_date"],format="mixed")
print(main_df["order_date"])
# print(main_df["order_date"].isna().sum())
#4
mo1 = main_df["order_date"].mode()[0]
# print(mo1)
main_df["order_date"]=main_df["order_date"].fillna(mo1)
print(main_df["order_date"])
#5
# print(main_df["quantity"])
main_df["quantity"] = pd.to_numeric(main_df["quantity"],errors= "coerce")
print(main_df["quantity"])
#6
mo2 = main_df["quantity"].median()
# print(mo2)
main_df["quantity"] = main_df["quantity"].fillna(mo2)
print(main_df['quantity'])

# print(main_df)
#7
print(main_df.duplicated().sum())
#8
# print(main_df["price"].isna().sum())
mo3  = round(main_df["price"].mean(),1)
print(mo3)
main_df["price"]= main_df["price"].fillna(mo3)





