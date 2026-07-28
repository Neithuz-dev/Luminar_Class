import pandas as pd
main_df = pd.read_csv(r"C:\Users\hp\Downloads\missing_data.csv")
# print(main_df)

main_df["Date"] = pd.to_datetime(main_df['Date'],format="mixed")

main_df = main_df.dropna(ignore_index = True)#ignore index will ignore the droped index and correct the index numbers
print(main_df)

m1 = main_df["Duration"].mode()[0]
print(m1)

main_df.loc[7,"Duration"] = m1
print(main_df)

m2 = main_df['Calories'].mean()
print(m2)

for i in main_df.index:
    if main_df.loc[i,"Calories"]>=400:
        main_df.loc[i,"Calories"] = m2
print(main_df)