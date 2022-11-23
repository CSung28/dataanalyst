import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#### Code that can use Korean on Seaborn, matplotlib on Mac
import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn as sns
%matplotlib inline

rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False

# Theme 1. Analysis Online Shopping Trend in 2022.01-09

# 1-1. Data load 

df1 = pd.read_excel('file_path/file_name.xlsx', sheet_name = 0)

# check data that it was brought well
df1

# check the columns
df1.columns

# When i bring the data, there was unnecessary row on the first.
# so I delete it with 'Indexing'.
df1 = df1[1:]

# Then i re-check the info.
df1.info()

# I can see that unnecessary row was deleted!

# Data Preprocessing
# change '시점'(date in string) into datetime 
df1['시점']

# There were strings in 8-9th value
# so change them and to datetime
df1['시점'] = ['2022-01', '2022-02', '2022-03', '2022-04', '2022-05', '2022-06', '2022-07', '2022-08', '2022-09']

df1['시점'] = pd.to_datetime(df1['시점'])

# check data
df1.head()

# make a 'month' column to do specific & simple analysis
df1['월'] = df1['시점'].dt.month

# check data 
df1.columns
