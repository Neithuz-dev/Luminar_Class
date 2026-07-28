import pandas as pd
main_df = pd.read_csv(r"C:\Users\hp\Downloads\missing_data.csv")
print(main_df)

main_df["Date"] = pd.to_datetime(main_df['Date'],format="mixed")
print(main_df['Date'].dtypes)