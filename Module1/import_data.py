import pandas as pd
import os
dirname=os.path.dirname

url="https://people.sc.fsu.edu/~jburkardt/data/csv/homes.csv"

data = pd.read_csv(url)
data = data.head(20)

data.to_csv("{}/data.csv".format(dirname(__file__)))

types= data.dtypes
print('$$ data.dtypes:\n\n', types, file=open('{}/data.dtypes.txt'.format(dirname(__file__)), 'w'))  

description = data.describe()
print('\n$$ data.describe()\n\n', description, file=open('{}/data.describe.txt'.format(dirname(__file__)), 'w'))  
description = data.describe(include="all")
print('\n\n\n$$ data.describe(include="all")\n\n', description, file=open('{}/data.describe.txt'.format(dirname(__file__)), 'a+'))  

info = data.info
print('$$ data.info:\n\n', info, file=open('{}/data.info.txt'.format(dirname(__file__)), 'w'))  
