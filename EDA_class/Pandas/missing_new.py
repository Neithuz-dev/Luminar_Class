import pandas as pd
main_df = pd.read_csv(r"C:\Users\hp\Downloads\missing_data.csv")
# print(main_df)

main_df["Date"] = pd.to_datetime(main_df['Date'],format="mixed")
print(main_df['Date'].dtypes)

m1 = main_df['Calories'].mean()
# print(m1)

main_df["Calories"] = main_df['Calories'].fillna(m1)
print(main_df)

m2 = main_df['Calories'].median()
print(m2)

print('-'*100)
mo2 = main_df["Date"].mode()[0] #[0] is used the mode date is given in data frame series so [0] will give the first value


main_df['Date'] = main_df["Date"].fillna(mo2)
print(main_df)

print(main_df.isna().sum())
