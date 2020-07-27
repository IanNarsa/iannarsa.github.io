#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import collections


# In[2]:


df = pd.read_csv("gempaInfo.csv")
df.head()


# In[3]:


df.columns


# In[4]:


date = []
time = []
timezone = []
text = []
htags = []

for i in range (len(df["tweet"])):
    if df["tweet"][i].find("#Gempa Mag:") != (-1):
        date.append(df["date"][i])
        time.append(df["time"][i])
        timezone.append(df["timezone"][i])
        text.append(df["tweet"][i])
        htags.append(df["hashtags"][i])


# In[5]:


dt = {"Date":date, "Time":time, "Timezone":timezone, "Tweet":text, "Hashtags":htags}
ndf = pd.DataFrame(dt)
print(ndf.head())



# In[6]:


tweets = ndf["Tweet"]


# In[7]:


mag = []
mag = []
for x in range (len(tweets)):
    a = tweets.values[x].split(",")
    try:
        a = a[0].split("#Gempa Mag:")[1]
        a = a.split(" ")
        a = a[0]
        mag.append(a[0])
    except:
        b = tweets.values[x]
        b = b.split(",")
        b = b[0].split("#Gempa Mag: ")
        mag.append(b[1])
        continue
dataMag = np.array(mag)
dataMag = dataMag.astype(np.float64)
dataMag.dtype
print(len(dataMag))


# In[8]:


mag = {"Magnitudo":dataMag}
ndf.update(mag)
ndf.keys()
print(ndf.head())


# In[9]:


tgl = []
jumlah = []

counter = collections.Counter(ndf["Date"])
for x in counter.keys():
    tgl.append(x)
for x in counter.values():
    jumlah.append(x)
dt = {"Date":tgl, "Total_Tweets":jumlah}
dfTweet = pd.DataFrame(dt)
dfTweet = dfTweet.set_index(["Date"])
dfTweet.head()


# In[10]:


len(dfTweet)


# In[11]:


dfTweet.plot(figsize = (30,10))
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.legend(fontsize = 20)
plt.show()

