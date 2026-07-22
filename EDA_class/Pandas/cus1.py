import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Downloads\customer1.txt" ,names= ['id','fname','lname', 'age','prof','loc'])
# print(df.sort_values(by= "fname",ascending= False))

df5 = (df.loc[df[loc]df.sort_values(by='age')[['']])