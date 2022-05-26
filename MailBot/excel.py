import pandas as pd

df = pd.read_excel('mailbot.xlsx')

for i in df.iterrows():
    name = i[1]["Name"]
    email = i[1]["email"]
    print(f'name {name}')
    print(f'email {email}')
