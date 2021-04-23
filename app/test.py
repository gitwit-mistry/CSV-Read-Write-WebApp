import pandas as pd

df = pd.DataFrame(columns=['fname','lname','age'],in)

df = pd.read_csv('sheets/sheet1.csv')

df = df.append({'fname':'ram','lname':'rraamm','age':101})

print(df)

df.to_csv('sheets/sheet1.csv')