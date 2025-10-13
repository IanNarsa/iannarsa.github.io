#!/usr/bin/env python
# coding: utf-8

# # Eksploratory Data Analysis Nilai Tukar Petani 2020
# 
# ## Penjelasan
# 
# Proyek ini terdapat data yang berasal dari Badan Pusat Statistik (BPS https://www.bps.go.id/), pada data ini memuat nilai tukar petani (NTP).
# 
# NTP sendiri merupakan indikator proxy kesejahteraan petani. NTP didapat dari perbandingan antara Indeks harga yg diterima petani (It) dengan Indeks harga yg dibayar petani (Ib).
# 
# NTP sendiri mempunyai arti yaitu sebegai berikut:
# 
# 1. NTP > 100, berarti petani mengalami surplus. Harga produksi naik lebih besar dari kenaikan harga konsumsinya. Pendapatan petani naik lebih besar dari pengeluarannya.
# 
# 2. NTP = 100, berarti petani mengalami impas. Kenaikan/penurunan harga produksinya sama dengan persentase kenaikan/penurunan harga barang konsumsi. Pendapatan petani sama dengan pengeluarannya.
# 
# 3. NTP < 100, berarti petani mengalami defisit. Kenaikan harga produksi relatif lebih kecil dibandingkan dengan kenaikan harga barang konsumsinya. Pendapatan petani turun, lebih kecil dari pengeluarannya.
# 
# Dari hasil Eploratory Data Analysis (EDA) diharapkan dapat menjadi sumber insight dalam pemberdayaan sektor pertanian.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import locale
from locale import atof
import numpy as np
import re
locale.setlocale(locale.LC_NUMERIC, '')


# In[2]:


data = pd.read_csv("data/NTP_2020.csv")


# In[3]:


data.head()


# In[4]:


data = data.replace('-',np.nan)
data = data.replace(np.nan, 0)


# In[5]:


print("Kelompok ",data["Kelompok"].unique())
print("Provinsi ",data["Provinsi"].unique())


# In[6]:


dfPangan = data[data["Kelompok"]=="Petani Tanaman Pangan"].drop(columns = "Kelompok").set_index('Provinsi').apply(lambda x: x.str.replace(',','.')).astype(float).replace(np.nan, 0)
dfHortikultura  = data[data["Kelompok"]=="Petani Hortikultura"].drop(columns = "Kelompok").set_index('Provinsi').apply(lambda x: x.str.replace(',','.')).astype(float).replace(np.nan, 0)
dfKebun = data[data["Kelompok"]=="Petani Tanaman Perkebunan"].drop(columns = "Kelompok").set_index('Provinsi').apply(lambda x: x.str.replace(',','.')).astype(float).replace(np.nan, 0)
dfPeternakan = data[data["Kelompok"]=="Petani Peternakan"].drop(columns = "Kelompok").set_index('Provinsi').apply(lambda x: x.str.replace(',','.')).astype(float).replace(np.nan, 0)
dfNelayan = data[data["Kelompok"]=="Nelayan"].drop(columns = "Kelompok").set_index('Provinsi').apply(lambda x: x.str.replace(',','.')).astype(float).replace(np.nan, 0)
dfBudIkan = data[data["Kelompok"]=="Pembudidayaan Ikan"].drop(columns = "Kelompok").set_index('Provinsi').apply(lambda x: x.str.replace(',','.')).astype(float).replace(np.nan, 0)
dfNelayandanBudidaya = data[data["Kelompok"]=="Nelayan dan Pembudidayaan Ikan"].drop(columns = "Kelompok").set_index('Provinsi').apply(lambda x: x.str.replace(',','.')).astype(float).replace(np.nan, 0)


# In[7]:


dfPProv = dfPangan.drop(index='INDONESIA')
dfHProv = dfHortikultura.drop(index='INDONESIA')
dfKprov = dfKebun.drop(index='INDONESIA')
dfTProv = dfPeternakan.drop(index='INDONESIA')
dfNProv = dfNelayan.drop(index='INDONESIA')
dfIProv = dfBudIkan.drop(index='INDONESIA')
dfNBProv = dfNelayandanBudidaya.drop(index='INDONESIA')


# In[8]:


print('Kelompok Tani Pangan')
print(dfPangan[dfPangan["Tahunan"]==dfPangan["Tahunan"].max()]["Tahunan"],'\n')
print('Kelompok Tani Hortikultura')
print(dfHortikultura[dfHortikultura["Tahunan"]==dfHortikultura["Tahunan"].max()]["Tahunan"],'\n')
print('Kelompok Perkebunan')
print(dfKebun[dfKebun["Tahunan"]==dfKebun["Tahunan"].max()]["Tahunan"],'\n')
print('Kelompok Peternakan')
print(dfPeternakan[dfPeternakan["Tahunan"]==dfPeternakan["Tahunan"].max()]["Tahunan"],'\n')
print('Kelompok Nelayan')
print(dfNelayan[dfNelayan["Tahunan"]==dfNelayan["Tahunan"].max()]["Tahunan"],'\n')
print('Kelompok Budidaya Ikan')
print(dfBudIkan[dfBudIkan["Tahunan"]==dfBudIkan["Tahunan"].max()]["Tahunan"],'\n')
print('Kelompok Nelayan dan Pembudidayaan Ikan')
print(dfNelayandanBudidaya[dfNelayandanBudidaya["Tahunan"]==dfNelayandanBudidaya["Tahunan"].max()]["Tahunan"],'\n')


# ## EDA Bagian Kelompok Petani Pangan

# In[9]:


print("======================== Statistika Deskriptif Kelompok Petani Pangan Seluruh Provinsi ========================")
dfPProv.drop(columns="Tahunan").describe()


# In[10]:


nasional = dfPangan.reset_index()
nasional = nasional[nasional["Provinsi"]=="INDONESIA"].drop(columns = "Tahunan").set_index('Provinsi').T['INDONESIA']


# In[ ]:


nasional


# In[11]:


plt.figure(figsize=(15,5))
plt.title('NTP Kelompok Tani Pangan Indonesia Tahun 2020')
plt.plot(nasional.index, nasional.values)


# In[12]:


data[data["Provinsi"]=="INDONESIA"].drop(["Tahunan", "Provinsi"], axis=1).set_index("Kelompok").T


# In[13]:


myData = data[data["Provinsi"]=="INDONESIA"].drop(["Tahunan", "Provinsi"], axis=1).set_index("Kelompok").T


# In[14]:


tamp = myData.apply(lambda x: x.str.replace(',','.')).astype(float).replace(np.nan, 0).rename(columns=lambda x: re.sub(' ','_',x))
tamp
#float(tamp.Petani["Januari"])


# In[26]:


plt.figure(figsize=(15,8))
plt.title('NTP Tahun 2020')
plt.plot(tamp.index, tamp["Nelayan"], label = "Nelayan")
plt.plot(tamp.index, tamp["Petani"], label = "Petani")
plt.plot(tamp.index, tamp["Petani_Tanaman_Perkebunan"], label = "Petani_Tanaman_Perkebunan")
plt.plot(tamp.index, tamp["Petani_Peternakan"], label = "Petani_Peternakan")
plt.legend()


# In[ ]:


# convert to csv (optional)
#dfPProv["Tahunan"].to_csv('dfPProv.csv')
data[data["Provinsi"]=="INDONESIA"].drop(["Tahunan", "Provinsi"], axis=1).set_index("Kelompok").T.to_csv("dfNasionalNTP.csv")


# In[16]:


dfPProv = dfPProv.reset_index()


# In[17]:


dfPProv["Tahunan"].describe()


# In[18]:


print("Daerah yang memiliki NTP tertinggi")
dfPProv[dfPProv["Tahunan"]==dfPProv["Tahunan"].max()]


# In[19]:


ab = dfPProv[dfPProv["Tahunan"]==dfPProv["Tahunan"].max()].drop(columns = "Tahunan").set_index('Provinsi').T['NUSA TENGGARA BARAT']
plt.figure(figsize=(15,5))
plt.title('NTP NUSA TENGGARA BARAT Tahun 2020')
plt.plot(ab.index, ab.values)


# In[20]:


print("Daerah yang memiliki NTP terendah")
dfPProv[dfPProv["Tahunan"]==dfPProv["Tahunan"].min()]


# In[21]:


print("========== Daftar Provinsi yang memiliki NTP di atas 100 ==========")
dfPProv[dfPProv["Tahunan"] > 100].sort_values(by=["Tahunan"], ascending=False)


# In[22]:


dfPProv[dfPProv["Tahunan"] > 100].sort_values(by=["Tahunan"], ascending=False)[['Provinsi','Tahunan']].set_index("Provinsi").plot(kind='bar', title ="NTP > 100", figsize=(10, 5), legend=True, fontsize=12)


# In[23]:


dfPProv[dfPProv["Tahunan"] > 100].sort_values(by=["Tahunan"], ascending=False)["Provinsi"]


# In[24]:


print("========== Daftar Provinsi yang memiliki NTP kisaran angka 100 ==========")
dfPProv[(dfPProv["Tahunan"] >99.9)&(dfPProv["Tahunan"] < 101)].sort_values(by=["Tahunan"], ascending=False)


# In[25]:


print("========== Daftar Provinsi yang memiliki NTP di bawah 100 ==========")
dfPProv[dfPProv["Tahunan"] < 100].sort_values(by=["Tahunan"], ascending=False)


# In[ ]:


dfPangan.T.INDONESIA

