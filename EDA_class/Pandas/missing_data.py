from datetime import datetime

import pandas as pd
main_df = pd.read_csv(r"C:\Users\hp\Downloads\missing_data.csv")
# print(main_df)



main_df['Calories'] = main_df["Calories"].fillna(300)
# print(main_df)
# print(main_df.isna().sum())

main_df['Date'] = pd.to_datetime(main_df['Date'],format= "mixed")
# print(main_df["Date"].dtypes)
# main_df["Date"] = main_df["Date"].fillna(datetime(2024,7,28))
# print(main_df.isna().sum())
# print(main_df)

main_df['Date'] = main_df["Date"].fillna(pd.Timestamp(2024 -7 -28))
print(main_df)
print(main_df.isna().sum())