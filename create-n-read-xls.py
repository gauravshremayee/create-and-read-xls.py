import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt

import numpy as np

df = pd.DataFrame({'a':[1,3,5,7,4,5,6,4,7,8,9],
                   'b':[3,5,6,2,4,6,7,8,7,8,9]})

writer = ExcelWriter('Pandas.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()

df = pd.read_excel('Pandas.xlsx', sheet_name='Sheet1')

sorted_by_gross = df.sort_values(['a'], ascending=False)

# y=10, x=9  y=9,x=8  y=3,x=7  y=8,x=7
print(sorted_by_gross['a'])

sorted_by_gross['a'].head(10).plot(kind="barh")
plt.show()
