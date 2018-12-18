import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')
web_stats = {'Day': [1, 2, 3, 4, 5, 6],
            'Visitors': [23, 32, 43, 12, 43, 22],
            'Bounce_Rate': [56, 65, 76, 89, 54, 90]}

df = pd.DataFrame(web_stats)

df.set_index('Day', inplace = True)
df['Visitors'].plot()
plt.show()

df.plot()
plt.show()
