import pandas as pd
import pickle

df = pd.DataFrame({'Date' : ['A', 'B', 'C', 'D', 'E'],
                    'Value': ['12', '34', '45', '32', '89']})

pickle_out = open('data.pickle', 'wb')
pickle.dump(df, pickle_out)
pickle_out.close()


pickle_in = open('data.pickle', 'rb')
df2 = pickle.load(pickle_in)
print(df2)
