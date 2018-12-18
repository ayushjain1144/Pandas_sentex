import pandas as pd

df = pd.DataFrame({'Date' : ['A', 'B', 'C', 'D', 'E'],
                    'Value': ['12', '34', '45', '32', '89']})

print(df)

df.to_csv('data1.csv')

# sending onlu 1 column to csv
df['Date'].to_csv('data2.csv')

#change name of all columns
df.columns = ['Alphabets','Value']
print(df)

#change name of 1 column
df.rename(columns = {'Alphabets': 'Date'}, inplace = True)
print(df)
