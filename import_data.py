import pandas as pd

url="http://samplecsvs.s3.amazonaws.com/SacramentocrimeJanuary2006.csv"

data = pd.read_csv(url)
data = data.head(20)

data.to_csv("./data.csv")

print('$$ data.dtypes:\n\n', data.dtypes, file = open('data.dtypes.txt', 'w'))  

print('\n$$ data.describe()\n\n', data.describe(), file = open('data.describe.txt', 'w'))  
print('\n\n\n$$ data.describe(include="all")\n\n', data.describe(include="all"), file = open('data.describe.txt', 'a+'))  

print('$$ data.info:\n\n', data.info, file = open('data.info.txt', 'w'))  
