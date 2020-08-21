
# Klustering penjualan supermarket


```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
```

Data set ini berisi data penjualan pada supermarket. Data set ini berisi beberapa atribut yang memuat informasi sebagai berikut.

1. Invoice id: id struk pembayaran
2. Branch: cabang supermarket, dalam hal ini terdapat 3 cabang A, B, C
3. City: Location of supercenters
4. Customer type: Jenis konsumen, konsumen yang terdaftar sebagai member atau tidak
5. Gender: Jenis kelamin konsumen
6. Product line: Kategori produk yang dijual - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel
7. Unit price: Harga produk dalam $
8. Quantity: Jumlah barang yang dijual
9. Tax: pajak sebesar 5% dari pembelian
10. Total: Total harga sudah termasuk pajak
11. Date: Tanggal transaksi
12. Time: Waktu transaksi (10am to 9pm)
13. Payment: Metode pembayaran yang dapat dilakukan oleh konsumen – Cash, Credit card dan Ewallet
14. COGS: Cost of goods sold
15. Gross margin percentage: Gross margin percentage
16. Gross income: Pendapatan kotor
17. Rating: Penilaian konsumen terhadap pengalaman berbelanja pada skala 1-10


```python
df = pd.read_csv("supermarket_sales.csv")
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Invoice ID</th>
      <th>Branch</th>
      <th>City</th>
      <th>Customer type</th>
      <th>Gender</th>
      <th>Product line</th>
      <th>Unit price</th>
      <th>Quantity</th>
      <th>Tax 5%</th>
      <th>Total</th>
      <th>Date</th>
      <th>Time</th>
      <th>Payment</th>
      <th>cogs</th>
      <th>gross margin percentage</th>
      <th>gross income</th>
      <th>Rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>750-67-8428</td>
      <td>A</td>
      <td>Yangon</td>
      <td>Member</td>
      <td>Female</td>
      <td>Health and beauty</td>
      <td>74.69</td>
      <td>7</td>
      <td>26.1415</td>
      <td>548.9715</td>
      <td>1/5/2019</td>
      <td>13:08</td>
      <td>Ewallet</td>
      <td>522.83</td>
      <td>4.761905</td>
      <td>26.1415</td>
      <td>9.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>226-31-3081</td>
      <td>C</td>
      <td>Naypyitaw</td>
      <td>Normal</td>
      <td>Female</td>
      <td>Electronic accessories</td>
      <td>15.28</td>
      <td>5</td>
      <td>3.8200</td>
      <td>80.2200</td>
      <td>3/8/2019</td>
      <td>10:29</td>
      <td>Cash</td>
      <td>76.40</td>
      <td>4.761905</td>
      <td>3.8200</td>
      <td>9.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>631-41-3108</td>
      <td>A</td>
      <td>Yangon</td>
      <td>Normal</td>
      <td>Male</td>
      <td>Home and lifestyle</td>
      <td>46.33</td>
      <td>7</td>
      <td>16.2155</td>
      <td>340.5255</td>
      <td>3/3/2019</td>
      <td>13:23</td>
      <td>Credit card</td>
      <td>324.31</td>
      <td>4.761905</td>
      <td>16.2155</td>
      <td>7.4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>123-19-1176</td>
      <td>A</td>
      <td>Yangon</td>
      <td>Member</td>
      <td>Male</td>
      <td>Health and beauty</td>
      <td>58.22</td>
      <td>8</td>
      <td>23.2880</td>
      <td>489.0480</td>
      <td>1/27/2019</td>
      <td>20:33</td>
      <td>Ewallet</td>
      <td>465.76</td>
      <td>4.761905</td>
      <td>23.2880</td>
      <td>8.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>373-73-7910</td>
      <td>A</td>
      <td>Yangon</td>
      <td>Normal</td>
      <td>Male</td>
      <td>Sports and travel</td>
      <td>86.31</td>
      <td>7</td>
      <td>30.2085</td>
      <td>634.3785</td>
      <td>2/8/2019</td>
      <td>10:37</td>
      <td>Ewallet</td>
      <td>604.17</td>
      <td>4.761905</td>
      <td>30.2085</td>
      <td>5.3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df["Date"] = pd.to_datetime(df["Date"])
```

Pada dataset tersebut, bahwa supermartket memiliki 3 cabang, cabang A berada di kota Yangon, cabang C berada di kota Naypitaw dan cabang B berada di kota Mandalay. Supermarket juga mengkelompokkan konsumennya mmenjadi dua yaitu member dan normal, konsumen dapat melakukan transaksi melalui Ewallet, Cash maupun Credit card. Supermarkat sendiri menjual enam jenis barang yaitu Health and beauty, Electronic accessories, Home and lifestyle,
 Sports and travel, Food and beverages dan Fashion accessories.


```python
print("Daftar Branch : ",df["Branch"].unique(),"\n")
print("Daftar Kota : ",df["City"].unique(),"\n")
print("Jenis Pelanggan : ",df["Customer type"].unique(),"\n")
print("Jenis Produk : ",df["Product line"].unique(),"\n")
print("Jenis Pembayaran : ",df["Payment"].unique(),"\n")
```

    Daftar Branch :  ['A' 'C' 'B'] 
    
    Daftar Kota :  ['Yangon' 'Naypyitaw' 'Mandalay'] 
    
    Jenis Pelanggan :  ['Member' 'Normal'] 
    
    Jenis Produk :  ['Health and beauty' 'Electronic accessories' 'Home and lifestyle'
     'Sports and travel' 'Food and beverages' 'Fashion accessories'] 
    
    Jenis Pembayaran :  ['Ewallet' 'Cash' 'Credit card'] 
    


Mencari kluster dari data penjualan, disini akan kita cari seperti apa perilaku konsumen dengan memilih dua variabel yaitu gross income dan Rating


```python
plt.figure(figsize=(20,10))
sns.scatterplot(x="gross income", 
                y="Rating", 
                data=df, s=100, color="red").set(title='Scatter plot Rating and Gross Income')
```




    [Text(0.5, 1.0, 'Scatter plot Rating and Gross Income')]




![png](output_8_1.png)



```python
dfc = df[["gross income","Rating"]]
dfc.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gross income</th>
      <th>Rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>26.1415</td>
      <td>9.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3.8200</td>
      <td>9.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>16.2155</td>
      <td>7.4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.2880</td>
      <td>8.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>30.2085</td>
      <td>5.3</td>
    </tr>
  </tbody>
</table>
</div>



Mencari Inertias, inertias diperlukan untuk mencari kluster yang tepat.


```python
X = np.array(list(zip(dfc["gross income"].values.astype(int),dfc["Rating"].values.astype(int)))).reshape(len(dfc["gross income"]),2)

inertias=[]
K= range(1,10)
for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(X)
    inertias.append(kmeanModel.inertia_)
plt.plot(K,inertias, 'bx-')
plt.show()
```


![png](output_11_0.png)


Dari grafik di atas patahan terjadi pada titik 3, sehingga pembagian kluster yang tepat adalah 3 kluster.


```python
x_array = np.array(dfc)
x_array
```




    array([[26.1415,  9.1   ],
           [ 3.82  ,  9.6   ],
           [16.2155,  7.4   ],
           ...,
           [ 1.592 ,  7.7   ],
           [ 3.291 ,  4.1   ],
           [30.919 ,  6.6   ]])




```python
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x_array)
x_scaled
```




    array([[0.52161615, 0.85      ],
           [0.06738704, 0.93333333],
           [0.31962801, 0.56666667],
           ...,
           [0.02204857, 0.61666667],
           [0.0566222 , 0.01666667],
           [0.6188354 , 0.43333333]])




```python
kmeans = KMeans(n_clusters = 3, random_state=123)
kmeans.fit(x_scaled)
```




    KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
           n_clusters=3, n_init=10, n_jobs=None, precompute_distances='auto',
           random_state=123, tol=0.0001, verbose=0)




```python
print(kmeans.cluster_centers_)
```

    [[0.67138402 0.38218391]
     [0.23963639 0.77755102]
     [0.17872797 0.27917695]]


## Hasil cluster


```python
df["kluster"] = kmeans.labels_
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Invoice ID</th>
      <th>Branch</th>
      <th>City</th>
      <th>Customer type</th>
      <th>Gender</th>
      <th>Product line</th>
      <th>Unit price</th>
      <th>Quantity</th>
      <th>Tax 5%</th>
      <th>Total</th>
      <th>Date</th>
      <th>Time</th>
      <th>Payment</th>
      <th>cogs</th>
      <th>gross margin percentage</th>
      <th>gross income</th>
      <th>Rating</th>
      <th>kluster</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>750-67-8428</td>
      <td>A</td>
      <td>Yangon</td>
      <td>Member</td>
      <td>Female</td>
      <td>Health and beauty</td>
      <td>74.69</td>
      <td>7</td>
      <td>26.1415</td>
      <td>548.9715</td>
      <td>2019-01-05</td>
      <td>13:08</td>
      <td>Ewallet</td>
      <td>522.83</td>
      <td>4.761905</td>
      <td>26.1415</td>
      <td>9.1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>226-31-3081</td>
      <td>C</td>
      <td>Naypyitaw</td>
      <td>Normal</td>
      <td>Female</td>
      <td>Electronic accessories</td>
      <td>15.28</td>
      <td>5</td>
      <td>3.8200</td>
      <td>80.2200</td>
      <td>2019-03-08</td>
      <td>10:29</td>
      <td>Cash</td>
      <td>76.40</td>
      <td>4.761905</td>
      <td>3.8200</td>
      <td>9.6</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>631-41-3108</td>
      <td>A</td>
      <td>Yangon</td>
      <td>Normal</td>
      <td>Male</td>
      <td>Home and lifestyle</td>
      <td>46.33</td>
      <td>7</td>
      <td>16.2155</td>
      <td>340.5255</td>
      <td>2019-03-03</td>
      <td>13:23</td>
      <td>Credit card</td>
      <td>324.31</td>
      <td>4.761905</td>
      <td>16.2155</td>
      <td>7.4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>123-19-1176</td>
      <td>A</td>
      <td>Yangon</td>
      <td>Member</td>
      <td>Male</td>
      <td>Health and beauty</td>
      <td>58.22</td>
      <td>8</td>
      <td>23.2880</td>
      <td>489.0480</td>
      <td>2019-01-27</td>
      <td>20:33</td>
      <td>Ewallet</td>
      <td>465.76</td>
      <td>4.761905</td>
      <td>23.2880</td>
      <td>8.4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>373-73-7910</td>
      <td>A</td>
      <td>Yangon</td>
      <td>Normal</td>
      <td>Male</td>
      <td>Sports and travel</td>
      <td>86.31</td>
      <td>7</td>
      <td>30.2085</td>
      <td>634.3785</td>
      <td>2019-02-08</td>
      <td>10:37</td>
      <td>Ewallet</td>
      <td>604.17</td>
      <td>4.761905</td>
      <td>30.2085</td>
      <td>5.3</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.columns
```




    Index(['Invoice ID', 'Branch', 'City', 'Customer type', 'Gender',
           'Product line', 'Unit price', 'Quantity', 'Tax 5%', 'Total', 'Date',
           'Time', 'Payment', 'cogs', 'gross margin percentage', 'gross income',
           'Rating', 'kluster'],
          dtype='object')



Scatterplot hasil klustering


```python
color_dict = dict({0:'brown',
                  1:'green',
                  2:'orange'})
plt.figure(figsize=(20,10))
sns.scatterplot(x="gross income", y="Rating", data=df, s=100, hue="kluster", palette=color_dict)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f4ee9b68588>




![png](output_21_1.png)


### Melihat deskripsi gross income pada setiap kluster


```python
dk0 = df[df["kluster"]==0].describe()["gross income"]
dk1 = df[df["kluster"]==1].describe()["gross income"]
dk2 = df[df["kluster"]==2].describe()["gross income"]
cc = pd.DataFrame({'kluster 0 gross income':dk0.values,
                   'kluster 1 gross income':dk1.values,
                   'kluster 2 gross income':dk2.values}, index=dk0.index)
cc
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>kluster 0 gross income</th>
      <th>kluster 1 gross income</th>
      <th>kluster 2 gross income</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>203.000000</td>
      <td>392.000000</td>
      <td>405.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>33.501318</td>
      <td>12.284592</td>
      <td>9.291460</td>
    </tr>
    <tr>
      <th>std</th>
      <td>7.407348</td>
      <td>8.217227</td>
      <td>5.895869</td>
    </tr>
    <tr>
      <th>min</th>
      <td>20.150000</td>
      <td>0.604500</td>
      <td>0.508500</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>27.519500</td>
      <td>5.985875</td>
      <td>4.125000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>33.421500</td>
      <td>10.162500</td>
      <td>8.377000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>39.110000</td>
      <td>18.277250</td>
      <td>13.962000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>49.650000</td>
      <td>37.300000</td>
      <td>23.090000</td>
    </tr>
  </tbody>
</table>
</div>



Jika dilihat dari tabel di atas, kluster 0 memiliki rata - rata pendapatan kotor tertinggi yaitu sebesar 33.5 dilanjutkan kluster 1 dengan rata - rata pendapatan kotor sebesar 12.28 dan yang terakhir kluster 2 sebesar 9.2.


```python
dk0 = df[df["kluster"]==0].describe()["Unit price"]
dk1 = df[df["kluster"]==1].describe()["Unit price"]
dk2 = df[df["kluster"]==2].describe()["Unit price"]
cc = pd.DataFrame({'kluster 0 Unit price':dk0.values,
                   'kluster 1 Unit price':dk1.values,
                   'kluster 2 Unit price':dk2.values}, index=dk0.index)
cc
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>kluster 0 Unit price</th>
      <th>kluster 1 Unit price</th>
      <th>kluster 2 Unit price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>203.000000</td>
      <td>392.000000</td>
      <td>405.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>81.134384</td>
      <td>51.377628</td>
      <td>47.066222</td>
    </tr>
    <tr>
      <th>std</th>
      <td>13.689975</td>
      <td>25.532772</td>
      <td>24.356520</td>
    </tr>
    <tr>
      <th>min</th>
      <td>40.300000</td>
      <td>10.130000</td>
      <td>10.080000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>72.435000</td>
      <td>30.135000</td>
      <td>25.560000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>82.880000</td>
      <td>50.255000</td>
      <td>45.350000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>92.340000</td>
      <td>72.585000</td>
      <td>64.970000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>99.960000</td>
      <td>99.830000</td>
      <td>99.890000</td>
    </tr>
  </tbody>
</table>
</div>



### Melihat deskripsi Rating setiap kluster


```python
desck0 = df[df["kluster"]==0].describe()["Rating"]
desck1 = df[df["kluster"]==1].describe()["Rating"]
desck2 = df[df["kluster"]==2].describe()["Rating"]

descdf = pd.DataFrame({"Rating Kluster 0 ":desck0.values,
                       "Rating Kluster 1 ":desck1.values,
                       "Rating Kluster 2 ":desck2.values}, index=desck0.index)
descdf
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rating Kluster 0</th>
      <th>Rating Kluster 1</th>
      <th>Rating Kluster 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>203.000000</td>
      <td>392.000000</td>
      <td>405.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>6.293103</td>
      <td>8.665306</td>
      <td>5.675062</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.493733</td>
      <td>0.793658</td>
      <td>0.937130</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.000000</td>
      <td>7.200000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>5.100000</td>
      <td>8.000000</td>
      <td>4.900000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>6.200000</td>
      <td>8.700000</td>
      <td>5.800000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>7.400000</td>
      <td>9.400000</td>
      <td>6.500000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>9.900000</td>
      <td>10.000000</td>
      <td>7.200000</td>
    </tr>
  </tbody>
</table>
</div>



Untuk rating setiap kluster dapat dilihat pada tabel di atas. Kluster 0 rata - rata memiliki rating 6.2, kluster 1 rata - rata memiliki rating 8.6 dan kluster 2 rata - rata memiliki rating 5.6.
 
 Jika kita lihat, dari tabel sebelumnya pendapatan kotor tertinggi ada pada kluster 0 sebesar 33.5 dan rata - rata rating 6.2 dan apabila kita lihat lagi pada kluster 0 ini juga memiliki rata - rata unit price yang tinggi yaitu sebesar  $81 . 
 
 Sementara untuk rata - rata rating tertinggi yang diberada pada kluster 1 sebesar 8.6 memiliki rata - rata pendapatan kotor 12.28, hal ini jauh di bawah rata - rata pendapatan kluster 0. Yang terakhir kluster 2 dengan rata - rata rating 5.6 dengan rata - rata pendapatan kotor 47.


```python
print("Kluster 0")
print(df[df["kluster"]==0].groupby(["Product line"])["Quantity", "gross income", "Rating"].sum(),"\n")
print("Kluster 1")
print(df[df["kluster"]==1].groupby(["Product line"])["Quantity", "gross income", "Rating"].sum(),"\n")
print("Kluster 2")
print(df[df["kluster"]==2].groupby(["Product line"])["Quantity", "gross income", "Rating"].sum(),"\n")
```

    Kluster 0
                            Quantity  gross income  Rating
    Product line                                          
    Electronic accessories       283     1115.3560   198.0
    Fashion accessories          269     1079.2110   207.1
    Food and beverages           270     1095.2255   201.0
    Health and beauty            251     1001.5165   201.0
    Home and lifestyle           319     1290.6620   237.2
    Sports and travel            300     1218.7965   233.2 
    
    Kluster 1
                            Quantity  gross income  Rating
    Product line                                          
    Electronic accessories       347      765.0105   557.8
    Fashion accessories          335      860.7085   603.7
    Food and beverages           369      898.9445   666.5
    Health and beauty            333      837.4175   553.2
    Home and lifestyle           327      724.3400   514.9
    Sports and travel            299      729.1390   500.7 
    
    Kluster 2
                            Quantity  gross income  Rating
    Product line                                          
    Electronic accessories       341      707.1350   421.4
    Fashion accessories          298      646.0755   440.4
    Food and beverages           313      679.3940   370.2
    Health and beauty            270      503.6250   310.3
    Home and lifestyle           265      549.8510   341.9
    Sports and travel            321      676.9610   414.2 
    



```python
df.describe().style.format("{:.3f}")
```




<style  type="text/css" >
</style><table id="T_de12534a_e3a6_11ea_a161_2973dcd2631a" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Unit price</th>        <th class="col_heading level0 col1" >Quantity</th>        <th class="col_heading level0 col2" >Tax 5%</th>        <th class="col_heading level0 col3" >Total</th>        <th class="col_heading level0 col4" >cogs</th>        <th class="col_heading level0 col5" >gross margin percentage</th>        <th class="col_heading level0 col6" >gross income</th>        <th class="col_heading level0 col7" >Rating</th>        <th class="col_heading level0 col8" >kluster</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_de12534a_e3a6_11ea_a161_2973dcd2631alevel0_row0" class="row_heading level0 row0" >count</th>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow0_col0" class="data row0 col0" >1000.000</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow0_col1" class="data row0 col1" >1000.000</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow0_col2" class="data row0 col2" >1000.000</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow0_col3" class="data row0 col3" >1000.000</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow0_col4" class="data row0 col4" >1000.000</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow0_col5" class="data row0 col5" >1000.000</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow0_col6" class="data row0 col6" >1000.000</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow0_col7" class="data row0 col7" >1000.000</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow0_col8" class="data row0 col8" >1000.000</td>
            </tr>
            <tr>
                        <th id="T_de12534a_e3a6_11ea_a161_2973dcd2631alevel0_row1" class="row_heading level0 row1" >mean</th>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow1_col0" class="data row1 col0" >55.672</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow1_col1" class="data row1 col1" >5.510</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow1_col2" class="data row1 col2" >15.379</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow1_col3" class="data row1 col3" >322.967</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow1_col4" class="data row1 col4" >307.587</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow1_col5" class="data row1 col5" >4.762</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow1_col6" class="data row1 col6" >15.379</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow1_col7" class="data row1 col7" >6.973</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow1_col8" class="data row1 col8" >1.202</td>
            </tr>
            <tr>
                        <th id="T_de12534a_e3a6_11ea_a161_2973dcd2631alevel0_row2" class="row_heading level0 row2" >std</th>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow2_col0" class="data row2 col0" >26.495</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow2_col1" class="data row2 col1" >2.923</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow2_col2" class="data row2 col2" >11.709</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow2_col3" class="data row2 col3" >245.885</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow2_col4" class="data row2 col4" >234.177</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow2_col5" class="data row2 col5" >0.000</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow2_col6" class="data row2 col6" >11.709</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow2_col7" class="data row2 col7" >1.719</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow2_col8" class="data row2 col8" >0.754</td>
            </tr>
            <tr>
                        <th id="T_de12534a_e3a6_11ea_a161_2973dcd2631alevel0_row3" class="row_heading level0 row3" >min</th>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow3_col0" class="data row3 col0" >10.080</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow3_col1" class="data row3 col1" >1.000</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow3_col2" class="data row3 col2" >0.508</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow3_col3" class="data row3 col3" >10.678</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow3_col4" class="data row3 col4" >10.170</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow3_col5" class="data row3 col5" >4.762</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow3_col6" class="data row3 col6" >0.508</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow3_col7" class="data row3 col7" >4.000</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow3_col8" class="data row3 col8" >0.000</td>
            </tr>
            <tr>
                        <th id="T_de12534a_e3a6_11ea_a161_2973dcd2631alevel0_row4" class="row_heading level0 row4" >25%</th>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow4_col0" class="data row4 col0" >32.875</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow4_col1" class="data row4 col1" >3.000</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow4_col2" class="data row4 col2" >5.925</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow4_col3" class="data row4 col3" >124.422</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow4_col4" class="data row4 col4" >118.497</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow4_col5" class="data row4 col5" >4.762</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow4_col6" class="data row4 col6" >5.925</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow4_col7" class="data row4 col7" >5.500</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow4_col8" class="data row4 col8" >1.000</td>
            </tr>
            <tr>
                        <th id="T_de12534a_e3a6_11ea_a161_2973dcd2631alevel0_row5" class="row_heading level0 row5" >50%</th>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow5_col0" class="data row5 col0" >55.230</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow5_col1" class="data row5 col1" >5.000</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow5_col2" class="data row5 col2" >12.088</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow5_col3" class="data row5 col3" >253.848</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow5_col4" class="data row5 col4" >241.760</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow5_col5" class="data row5 col5" >4.762</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow5_col6" class="data row5 col6" >12.088</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow5_col7" class="data row5 col7" >7.000</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow5_col8" class="data row5 col8" >1.000</td>
            </tr>
            <tr>
                        <th id="T_de12534a_e3a6_11ea_a161_2973dcd2631alevel0_row6" class="row_heading level0 row6" >75%</th>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow6_col0" class="data row6 col0" >77.935</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow6_col1" class="data row6 col1" >8.000</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow6_col2" class="data row6 col2" >22.445</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow6_col3" class="data row6 col3" >471.350</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow6_col4" class="data row6 col4" >448.905</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow6_col5" class="data row6 col5" >4.762</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow6_col6" class="data row6 col6" >22.445</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow6_col7" class="data row6 col7" >8.500</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow6_col8" class="data row6 col8" >2.000</td>
            </tr>
            <tr>
                        <th id="T_de12534a_e3a6_11ea_a161_2973dcd2631alevel0_row7" class="row_heading level0 row7" >max</th>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow7_col0" class="data row7 col0" >99.960</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow7_col1" class="data row7 col1" >10.000</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow7_col2" class="data row7 col2" >49.650</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow7_col3" class="data row7 col3" >1042.650</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow7_col4" class="data row7 col4" >993.000</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow7_col5" class="data row7 col5" >4.762</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow7_col6" class="data row7 col6" >49.650</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow7_col7" class="data row7 col7" >10.000</td>
                        <td id="T_de12534a_e3a6_11ea_a161_2973dcd2631arow7_col8" class="data row7 col8" >2.000</td>
            </tr>
    </tbody></table>



Melihat kluster 0


```python
print(df[df["kluster"]==0].groupby(["Gender"]).kluster.count())
ax = sns.countplot(x="Gender", data=df[df["kluster"]==0])
```

    Gender
    Female    109
    Male       94
    Name: kluster, dtype: int64



![png](output_32_1.png)



```python
print("Kluster 0 dengan pengkelompokan Gender dan Payment")
print(df[(df["kluster"]==0)].groupby(["Gender","Payment"]).kluster.count())
print("\nKluster 0 dengan pengkelompokan Gender dan Product line")
print(df[(df["kluster"]==0)].groupby(["Gender","Product line"]).kluster.count())
```

    Kluster 0 dengan pengkelompokan Gender dan Payment
    Gender  Payment    
    Female  Cash           36
            Credit card    40
            Ewallet        33
    Male    Cash           35
            Credit card    28
            Ewallet        31
    Name: kluster, dtype: int64
    
    Kluster 0 dengan pengkelompokan Gender dan Product line
    Gender  Product line          
    Female  Electronic accessories    16
            Fashion accessories       15
            Food and beverages        21
            Health and beauty         13
            Home and lifestyle        24
            Sports and travel         20
    Male    Electronic accessories    17
            Fashion accessories       17
            Food and beverages        10
            Health and beauty         18
            Home and lifestyle        15
            Sports and travel         17
    Name: kluster, dtype: int64


Melihat kluster 1


```python
print(df[df["kluster"]==1].groupby(["Gender"]).kluster.count())
ax = sns.countplot(x="Gender", data=df[df["kluster"]==1])
```

    Gender
    Female    202
    Male      190
    Name: kluster, dtype: int64



![png](output_35_1.png)



```python
print("Kluster 1 dengan pengkelompokan Gender dan Payment")
print(df[(df["kluster"]==1)].groupby(["Gender","Payment"]).kluster.count())
print("\nKluster 1 dengan pengkelompokan Gender dan Product line")
print(df[(df["kluster"]==1)].groupby(["Gender","Product line"]).kluster.count())
```

    Kluster 1 dengan pengkelompokan Gender dan Payment
    Gender  Payment    
    Female  Cash           81
            Credit card    61
            Ewallet        60
    Male    Cash           53
            Credit card    65
            Ewallet        72
    Name: kluster, dtype: int64
    
    Kluster 1 dengan pengkelompokan Gender dan Product line
    Gender  Product line          
    Female  Electronic accessories    31
            Fashion accessories       44
            Food and beverages        41
            Health and beauty         29
            Home and lifestyle        29
            Sports and travel         28
    Male    Electronic accessories    33
            Fashion accessories       25
            Food and beverages        37
            Health and beauty         35
            Home and lifestyle        31
            Sports and travel         29
    Name: kluster, dtype: int64


Melihat kluster 2


```python
print(df[df["kluster"]==2].groupby(["Gender"]).kluster.count())
ax = sns.countplot(x="Gender", data=df[df["kluster"]==2])
```

    Gender
    Female    190
    Male      215
    Name: kluster, dtype: int64



![png](output_38_1.png)



```python
print("Kluster 2 dengan pengkelompokan Gender dan Payment")
print(df[(df["kluster"]==2)].groupby(["Gender","Payment"]).kluster.count())
print("\nKluster 2 dengan pengkelompokan Gender dan Product line")
print(df[(df["kluster"]==2)].groupby(["Gender","Product line"]).kluster.count())
```

    Kluster 2 dengan pengkelompokan Gender dan Payment
    Gender  Payment    
    Female  Cash           61
            Credit card    62
            Ewallet        67
    Male    Cash           78
            Credit card    55
            Ewallet        82
    Name: kluster, dtype: int64
    
    Kluster 2 dengan pengkelompokan Gender dan Product line
    Gender  Product line          
    Female  Electronic accessories    37
            Fashion accessories       37
            Food and beverages        28
            Health and beauty         22
            Home and lifestyle        26
            Sports and travel         40
    Male    Electronic accessories    36
            Fashion accessories       40
            Food and beverages        37
            Health and beauty         35
            Home and lifestyle        35
            Sports and travel         32
    Name: kluster, dtype: int64

