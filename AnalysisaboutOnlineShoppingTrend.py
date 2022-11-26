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

# Theme 2. Analysis 22. 1. ~ 9.
# I will write two codes about analysis that i did
# (1) Computer

sns.lineplot(x = '월', y = '컴퓨터 및 주변기기', data = df1)
plt.title('컴퓨터 및 주변기기 거래액 총계')


fig, ax = plt.subplots(ncols = 2, figsize = (20, 10))
sns.lineplot(x = '월', y = '컴퓨터 및 주변기기.1', data = df1, ax = ax[0])
ax[0].set_title('컴퓨터 및 주변기기 거래액(인터넷 쇼핑)')
sns.lineplot(x = '월', y = '컴퓨터 및 주변기기.2', data = df1, ax = ax[1])
ax[1].set_title('컴퓨터 및 주변기기 거래액(모바일 쇼핑)')
plt.show()

# (2) Dairy, Farm, Seafood

fig = plt.figure(figsize = (10, 10))

ax1 = fig.add_subplot(211)
ax1.plot('월', '농축수산물', data = df1)
ax1.set_title('농축수산물 거래액 총계', fontsize = 14)

ax2 = fig.add_subplot(223)
ax2.plot('월', '농축수산물.1', data = df1)
ax2.set_title('농축수산물 거래액(인터넷 쇼핑)', fontsize = 14)

ax3 = fig.add_subplot(224)
ax3.plot('월', '농축수산물.2', data = df1)
ax3.set_title('농축수산물 거래액(모바일 쇼핑)', fontsize = 14)

plt.tight_layout()
plt.show()
