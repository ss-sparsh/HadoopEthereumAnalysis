#This the code from py notebook used for plotting

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time 
import datetime 

df = pd.read_csv(“outTemp.txt",header=None)

new = df[1].str.split("\t", n = 1, expand = True) 
df["year"]= new[0]
df["val"] = new[1]
df.drop(columns =[1], inplace = True) 

df[0] = df[0].str.strip('[ ')
df['year'] = df['year'].str.strip(' ]’)

df["month"] = df[0] +'/'+ df['year']
df['month'] = pd.to_datetime(df['month'], format=‘%m/%Y')
df.drop(columns =[0,'year'], inplace = True) 
df['val'] = df['val'].astype(float) 

df.sort_values(by=['month'],inplace=True)
df.plot.bar('month','val')