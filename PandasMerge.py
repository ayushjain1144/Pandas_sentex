import pandas as pd

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])


print(pd.merge(df1, df3, on = 'HPI'))
print(pd.merge(df1, df2, on = ['HPI', 'Int_rate']))


df1.set_index('HPI', inplace = True)
df2.set_index('HPI', inplace = True)
#here indec will go away! sed lyf:(
print(pd.merge(df1, df2, on = ['Int_rate']))

#But this world is full of hope :)

df4 = df1.join(df2)
print(df4)
