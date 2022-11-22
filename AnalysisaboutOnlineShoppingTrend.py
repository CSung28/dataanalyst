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


 
