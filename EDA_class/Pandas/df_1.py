import pandas as pd
employee = {"id":[101,102,103,104],"name":["ajin","anu" ,"vijay","vimal"]}

df = pd.DataFrame(employee)
print(df)
print(df.shape)
print(df.columns)