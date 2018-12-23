import pandas as pd
import numpy as np
import os
dirname=os.path.dirname


url="https://people.sc.fsu.edu/~jburkardt/data/csv/homes.csv"


data = pd.read_csv("{}/data.csv".format(dirname(__file__)))

#data = pd.read_csv(url)
#data = data.head(30)
#data.to_csv("{}/data.csv".format(dirname(__file__)))

#delet entries
data2 = data.dropna(subset=['Sell'], axis=0)  #axis=1 to delete the column

#replace a value
mean = data2["Age"].astype("float").mean(axis = 0)
data2["Age"].replace(np.nan,mean,inplace=True)

data2.to_csv("{}/analizedData.csv".format(dirname(__file__)))

#Binning
binwidth = int((max(data['Rooms']) - min(data["Rooms"])) / 3)
print(binwidth)

bins = np.arange( min(data['Rooms']), max(data["Rooms"])+binwidth, binwidth)
print(bins)

groupNames = ["low","medium","high"]
column = pd.cut( data2['Rooms'], bins, labels=groupNames)
print(column)