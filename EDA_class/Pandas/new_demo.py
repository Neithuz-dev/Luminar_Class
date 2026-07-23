import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Downloads\customer1.txt" ,names= ['id','fname','lname', 'age','prof','loc'])
print(df)

print(df.isna().sum())
df = df.fillna("india")
print(df.isna().sum())

