# **Analisis #Gempa @infoBMKG**
&nbsp;

Pada studi kasus ini kita akan menganalisa mengenai Gempa yang terjadi dari awal tahun 2018 sampai bulan 27 Juli 2020. Data ini bersumber dari akun twitter @infoBMKG yang diambil dengan kata kunci #Gempa. Tujuan dari analisa ini adalah agar dapat dimanfaatkannya limpahan Big Data yang bersumber dari twitter dengan fokus topik mengenai gempa. Dengan kita mengetahui wilayah mana saja yang pernah terjadi gempa, kita dapat melakukan mitigasi bencana pada wilayah - wilayah tersebut. 
<br>
Dalam proses analisis ini kita juga melakukan proses ETL (Extract Transfom Load), ekstrasi data dari twitter kemudian ditransform menjadi format baru sesuai keutuhan lalu disimpan dalam variabel yang telah ditentukan. File disimpan dalam format .csv kemudian kita perlu mengetahui terdapat kolom apa saja, kita cukup melihat nama - nama kolom.
&nbsp;
&nbsp;

Detail kolom dari data frame di atas dapat dilihat di bawah ini. 


    Index(['id', 'conversation_id', 'created_at', 'date', 'time', 'timezone',
           'user_id', 'username', 'name', 'place', 'tweet', 'mentions', 'urls',
           'photos', 'replies_count', 'retweets_count', 'likes_count', 'hashtags',
           'cashtags', 'link', 'retweet', 'quote_url', 'video', 'near', 'geo',
           'source', 'user_rt_id', 'user_rt', 'retweet_id', 'reply_to',
           'retweet_date', 'translate', 'trans_src', 'trans_dest'],
          dtype='object')



## Preprocessing
 
Setelah data dapat diekstrak atau dibuka, data yang ada ditransform sesuai dengan kebutuhan analis. Pada tahap ini dipilah lagi tweet yang ada, kita hanya akan mengambil data tanggal pada kolom date, waktu pada kolom time, waktu wilayah pada kolom timezone dan tweet pada kolom tweet, tweet yang diambil hanya tweet yang menginformasikan gempa. Untuk mengetahuinya kita dapat melihat pada tweet apakah ada kalimat '#Gempa Mag:' yang menandakan tweet tersebut menginformasikan kejadian mengenai gempa.


             Date      Time Timezone                                               Tweet
    0  2020-07-27  08:27:05      WIB   #Gempa Mag:5, 27/07/2020 05:01:23 (Pusat gempa...
    1  2020-07-27  08:25:52      WIB   #Gempa Mag:5.0, 27-Jul-20 05:01:23 WIB, Lok:0....
    2  2020-07-27  05:09:05      WIB   #Gempa Mag:5.0, 27-Jul-20 05:01:23 WIB, Lok:0....
    3  2020-07-27  05:05:58      WIB   #Gempa Mag:5.0, 27-Jul-20 05:01:23 WIB, Lok:0....
    4  2020-07-26  21:39:05      WIB   #Gempa Mag:3.2, 26/07/2020 21:18:14 (Pusat gem...

&nbsp;


Data teks dari kolom tweet kita ambil untuk kita pilah kembali untuk menemukan tweet yang berkaitan dengan pemberitaan gempa bumi yang terjadi, karena belum tentu tweet yang mengandung #Gempa itu memberitakan bencana gempa bisa saja memberitakan informasi tentang apa itu gempa? atau klarifikasi berita gempa. Dalam proses ini kita mencari kalimat "#Gempa Mag:" apabila ada kalimat tersebut maka tweet tersebut memberitakan gempa bumi yang terjadi.
<br>
<br>
Selain itu kita juga akan menambah kolom "Area" yang berisi informasi dimana gempa terjadi. 
<br>

## Visualisasi dan Analisa

Data yang sudah melalui tahap preprocessing akan menghasilkan seperti tabel di bawah ini. Di sini terdapat 5 kolom yaitu Date yang berisi tanggal tweet dipublish, Time yang berisi waktu tweet dipublish, Timezone, zona waktu untuk Time, Magnitudo dan Area


|  | Date | Time | Timezone | Magnitudo | Area |
| --- | --- | --- | --- | --- | --- |
| 0 | 2020-07-27 | 08:27:05 | WIB | 5.0 | Pusat gempa di laut 89 km Timur Laut Nias Sela... |
| 1 | 2020-07-27 | 08:25:52 | WIB | 5.0 | Pusat gempa berada di laut 89 km Timur Laut Ni... |
| 2 | 2020-07-27 | 05:09:05 | WIB | 5.0 | 89 km TimurLaut NIASSELATAN-SUMUT, Kedalaman:1... |
| 3 | 2020-07-27 | 05:05:58 | WIB | 5.0 | 89 km TimurLaut NIASSELATAN-SUMUT, Kedlmn:10 K... |
| 4 | 2020-07-26 | 21:39:05 | WIB | 3.2 | Pusat gempa di laut 22 km Barat Laut Lembata, ... |


<br>

| Date | Total_Tweets|
| --- | --- |
| 2018-01-01 | 5 |
| 2018-01-03 | 2 |
| 2018-01-04 | 6 |
| 2018-01-05 | 5 |
| 2018-01-06 | 6 |

<br>
    5 Tweet Tertinggi 
    
                Total_Tweets
    Date                    
    2018-11-15            82
    2019-11-15            69
    2019-09-26            64
    2018-11-09            51
    2018-10-02            49 
    
    Total hari 	:  858 
    
    Banyak Tweet 	:  7504 
    


Selama 858 hari BMKG melakukan tweet sebanyak 7504 tweet mengenai #Gempa, jumlah tweet terbanyak terjadi pada tanggal 15 November 2018 yaitu sebanyak 82 Tweet. 
<br> 
<br>
Di bawah merupakan grafik garis frekuensi tweet setiap harinya selama periode Januari 2018 sampai 27 Juli 2020


![png](graph.png)


&nbsp;
Dari keseluruhan data didapat rata - rata, median dan modulus sebesar :

    mean    : 4.323960554370998
    median  : 4.5
    mode    : 5.0
    dtype   : float64


Data yang ditampilkan pada tabel berikut merupakan gempa yang terjadi dengan kekuatan 7 skala richter ke atas. Jika dilihat tempat yang pernah dilanda gempa 7 skala richter ke atas rata - rata terjadi pada wilayah Indonesia bagian Timur, tapi bukan berarti wilayah lain aman dari bencana gempa bumi.
 

|  | Date | Time | Timezone | Magnitudo | Area |
| --- | --- | --- | --- | --- | --- |
| 45 | 2020-07-17 | 10:03:04 | WIB | 7.3 | 192 km TimurLaut PORTMORESBY-PNG, Kedalaman:87... |
| 46 | 2020-07-17 | 10:01:18 | WIB | 7.3 | 192 km TimurLaut PORTMORESBY-PNG, Kedlmn:87 Km... |
| 296 | 2020-06-04 | 16:18:05 | WIB | 7.1 | Pusat gempa di laut 89 km BaratLaut Daruba, Ke... |
| 297 | 2020-06-04 | 15:57:05 | WIB | 7.1 | 89 km BaratLaut DARUBA-MALUT, Kedalaman:112 Km... |
| 298 | 2020-06-04 | 15:54:25 | WIB | 7.1 | 89 km BaratLaut DARUBA-MALUT, Kedlmn:112 Km, t... |
| 442 | 2020-05-06 | 21:00:05 | WIB | 7.3 | 180 km BaratLaut MALUKUTENGGARABRT, Kedalaman:... |
| 443 | 2020-05-06 | 20:59:20 | WIB | 7.3 | 180 km BaratLaut MALUKUTENGGARABRT, Kedlmn:133... |
| 1708 | 2019-11-15 | 00:06:22 | WIB | 7.4 | Pusat gempa berada dilaut 134 BaratLaut Jailol... |
| 1709 | 2019-11-15 | 00:06:09 | WIB | 7.4 | Pusat gempa dilaut 134 BaratLaut Jailolo, Kedl... |
| 1710 | 2019-11-14 | 23:36:10 | WIB | 7.1 | 137 km BaratLaut JAILOLO-MALUT, Kedalaman:73 K... |
| 1711 | 2019-11-14 | 23:27:11 | WIB | 7.4 | 134 km BaratLaut JAILOLO-MALUT, Kedalaman:10 K... |
| 2766 | 2019-08-02 | 19:13:42 | WIB | 7.4 | 147 km BaratDaya SUMUR-BANTEN, Kedalaman:10 Km... |
| 2767 | 2019-08-02 | 19:09:30 | WIB | 7.4 | 147 km BaratDaya SUMUR-BANTEN, Kedalaman:10 Km... |
| 2925 | 2019-07-14 | 16:36:12 | WIB | 7.2 | Pusat gempa di darat 62km TimurLaut Labuha, Ke... |
| 2926 | 2019-07-14 | 16:36:12 | WIB | 7.2 | Pusat gempa berada di darat 62km TimurLaut Lab... |
| 2929 | 2019-07-14 | 16:18:08 | WIB | 7.2 | 62 km TimurLaut LABUHA-MALUT, Kedalaman:10 Km,... |
| 2930 | 2019-07-14 | 16:15:44 | WIB | 7.2 | 62 km TimurLaut LABUHA-MALUT, Kedlmn:10 Km, td... |
| 2969 | 2019-07-07 | 23:03:19 | WIB | 7.1 | Pusat gempa berada di laut 136 km Barat Daya T... |
| 2970 | 2019-07-07 | 23:03:08 | WIB | 7.1 | Pusat gempa di laut 136 km Barat Daya Ternate,... |
| 2971 | 2019-07-07 | 22:24:07 | WIB | 7.0 | 133 km BaratDaya TERNATE-MALUT, Kedalaman:36 K... |
| 2972 | 2019-07-07 | 22:21:10 | WIB | 7.1 | 135 km BaratDaya TERNATE-MALUT, Kedalaman:10 K... |
| 2973 | 2019-07-07 | 22:14:01 | WIB | 7.1 | 136 km BaratDaya TERNATE-MALUT, Kedlmn:10 Km, ... |
| 3068 | 2019-06-24 | 10:00:08 | WIB | 7.7 | 245 km TimurLaut MALUKUBRTDAYA, Kedalaman:231 ... |
| 3069 | 2019-06-24 | 09:58:07 | WIB | 7.7 | 245 km TimurLaut MALUKUBRTDAYA, Kedlmn:231 Km,... |
| 4396 | 2018-12-29 | 12:59:02 | WIB | 7.1 | Pusat gempa berada di laut Mindanao - Philipin... |
| 5832 | 2018-09-28 | 17:09:11 | WIB | 7.7 | 27 km TimurLaut DONGGALA-SULTENG, Kedalaman:10... |
| 6321 | 2018-08-05 | 19:46:09 | WIB | 7.0 | Pusat gempa di darat 18 km Barat Laut Lombok T... |
| 6322 | 2018-08-05 | 19:36:10 | WIB | 7.0 | Pusat gempa di darat 18 km Barat Laut Lombok T... |
| 7279 | 2018-02-26 | 01:31:11 | WIB | 7.6 | Pusat gempa di darat 266 km tenggara Bovendigo... |
| 7280 | 2018-02-26 | 01:29:42 | WIB | 7.6 | Pusat gempa berada di darat 266 km tenggara Bo... |
| 7283 | 2018-02-26 | 00:52:11 | WIB | 7.6 | 266 km Tenggara BOVENDIGOEL-PAPUA, Kedlmn:96 K... |
| 7284 | 2018-02-26 | 00:51:10 | WIB | 7.6 | 266 km Tenggara BOVENDIGOEL-PAPUA, Kedlmn:96 Km |

```
    array([['2020-07-17', '10:03:04', 'WIB', 7.3,
            '192 km TimurLaut PORTMORESBY-PNG, Kedalaman:87 Km, tidak berpotensi tsunami '],
           ['2020-07-17', '10:01:18', 'WIB', 7.3,
            '192 km TimurLaut PORTMORESBY-PNG, Kedlmn:87 Km, tdk berpotensi tsunami '],
           ['2020-06-04', '16:18:05', 'WIB', 7.1,
            'Pusat gempa di laut 89 km BaratLaut Daruba, Kedlmn:112 Km Dirasakan ,MMI IV Morotai, II-III Manado, II-III Bitung, II-III Minahasa, II-III Ternate, II-III Sitaro, II-III Tahuna, II-III Talaud, II-III Bolaang Mongondow , '],
           ['2020-06-04', '15:57:05', 'WIB', 7.1,
            '89 km BaratLaut DARUBA-MALUT, Kedalaman:112 Km, tidak berpotensi tsunami '],
           ['2020-06-04', '15:54:25', 'WIB', 7.1,
            '89 km BaratLaut DARUBA-MALUT, Kedlmn:112 Km, tdk berpotensi tsunami '],
           ['2020-05-06', '21:00:05', 'WIB', 7.3,
            '180 km BaratLaut MALUKUTENGGARABRT, Kedalaman:133 Km, tidak berpotensi tsunami '],
           ['2020-05-06', '20:59:20', 'WIB', 7.3,
            '180 km BaratLaut MALUKUTENGGARABRT, Kedlmn:133 Km, tdk berpotensi tsunami '],
           ['2019-11-15', '00:06:22', 'WIB', 7.4,
            'Pusat gempa berada dilaut 134 BaratLaut Jailolo, Kedlmn:10 Km Dirasakan ,MMI IV-V Bitung, IV-V Manado, III-IV Gorontalo, III-IV Ternate, II Buol '],
           ['2019-11-15', '00:06:09', 'WIB', 7.4,
            'Pusat gempa dilaut 134 BaratLaut Jailolo, Kedlmn:10 Km Dirasakan ,MMI IV-V Bitung, IV-V Manado, III-IV Gorontalo, III-IV Ternate, II Buol, '],
           ['2019-11-14', '23:36:10', 'WIB', 7.1,
            '137 km BaratLaut JAILOLO-MALUT, Kedalaman:73 Km, Potensi tsunami utk dtrskn pd msyrkt '],
           ['2019-11-14', '23:27:11', 'WIB', 7.4,
            '134 km BaratLaut JAILOLO-MALUT, Kedalaman:10 Km, Potensi tsunami utk dtrskn pd msyrkt '],
           ['2019-08-02', '19:13:42', 'WIB', 7.4,
            '147 km BaratDaya SUMUR-BANTEN, Kedalaman:10 Km, Potensi tsunami utk dtrskn pd msyrkt '],
           ['2019-08-02', '19:09:30', 'WIB', 7.4,
            '147 km BaratDaya SUMUR-BANTEN, Kedalaman:10 Km, Potensi tsunami utk dtrskn pd msyrkt '],
           ['2019-07-14', '16:36:12', 'WIB', 7.2,
            'Pusat gempa di darat 62km TimurLaut Labuha, Kedlmn:10 Km Dirasakan ,MMI V Obi, III Labuha, II-III Manado, II-III Ambon, II Ternate, II Namlea, II Gorontalo, II Sorong, II Bolang Mongondow, '],
           ['2019-07-14', '16:36:12', 'WIB', 7.2,
            'Pusat gempa berada di darat 62km TimurLaut Labuha, Kedlmn:10 Km Dirasakan ,MMI V Obi, III Labuha, II-III Manado, II-III Ambon, II Ternate, II Namlea, II Gorontalo, II Sorong, II Bolang Mongondow '],
           ['2019-07-14', '16:18:08', 'WIB', 7.2,
            '62 km TimurLaut LABUHA-MALUT, Kedalaman:10 Km, tidak berpotensi tsunami '],
           ['2019-07-14', '16:15:44', 'WIB', 7.2,
            '62 km TimurLaut LABUHA-MALUT, Kedlmn:10 Km, tdk berpotensi tsunami '],
           ['2019-07-07', '23:03:19', 'WIB', 7.1,
            'Pusat gempa berada di laut 136 km Barat Daya Ternate, Kedlmn:10 Km Dirasakan ,MMI IV-V Bitung, IV-V Manado, III-IV Ternate '],
           ['2019-07-07', '23:03:08', 'WIB', 7.1,
            'Pusat gempa di laut 136 km Barat Daya Ternate, Kedlmn:10 Km Dirasakan ,MMI IV-V Bitung, IV-V Manado, III-IV Ternate, '],
           ['2019-07-07', '22:24:07', 'WIB', 7.0,
            '133 km BaratDaya TERNATE-MALUT, Kedalaman:36 Km, Potensi tsunami utk dtrskn pd msyrkt '],
           ['2019-07-07', '22:21:10', 'WIB', 7.1,
            '135 km BaratDaya TERNATE-MALUT, Kedalaman:10 Km, Potensi tsunami utk dtrskn pd msyrkt '],
           ['2019-07-07', '22:14:01', 'WIB', 7.1,
            '136 km BaratDaya TERNATE-MALUT, Kedlmn:10 Km, tdk berpotensi tsunami '],
           ['2019-06-24', '10:00:08', 'WIB', 7.7,
            '245 km TimurLaut MALUKUBRTDAYA, Kedalaman:231 Km, tidak berpotensi tsunami '],
           ['2019-06-24', '09:58:07', 'WIB', 7.7,
            '245 km TimurLaut MALUKUBRTDAYA, Kedlmn:231 Km, tdk berpotensi tsunami '],
           ['2018-12-29', '12:59:02', 'WIB', 7.1,
            'Pusat gempa berada di laut Mindanao - Philipina, Kedlmn:69 Km Dirasakan ,MMI IV Talaud, III-IV Tahuna, III- IV Sangihe, III Siau Sitaro, III Tobelo, III Morotai , II Manado, II Ternate, II Jailolo '],
           ['2018-09-28', '17:09:11', 'WIB', 7.7,
            '27 km TimurLaut DONGGALA-SULTENG, Kedalaman:10 Km, Potensi tsunami utk dtrskn pd msyrkt '],
           ['2018-08-05', '19:46:09', 'WIB', 7.0,
            'Pusat gempa di darat 18 km Barat Laut Lombok Timur, Kedlmn:15 Km Dirasakan ,MMI III Waingapu, II Sawahan, II-III Banyuwangi, V-VI Denpasar, IV Kuta, II-III Situbondo, V-VI Karangasem, V-VI Bima, II-III Malang, VII Mataram, '],
           ['2018-08-05', '19:36:10', 'WIB', 7.0,
            'Pusat gempa di darat 18 km Barat Laut Lombok Timur, Kedlmn:15 Km Dirasakan ,MMI III Waingapu, II Sawahan, II-III Banyuwangi, V-VI Denpasar, IV Kuta, II-III Situbondo, V-VI Karangasem, V-VI Bima, II-III Malang, '],
           ['2018-02-26', '01:31:11', 'WIB', 7.6,
            'Pusat gempa di darat 266 km tenggara Bovendigoel, Kedlmn:96 Km Dirasakan ,MMI IV-V Tanah Merah, IV-V Wamena, IV-V Merauke, II-III Jayapura, '],
           ['2018-02-26', '01:29:42', 'WIB', 7.6,
            'Pusat gempa berada di darat 266 km tenggara Bovendigoel, Kedlmn:96 Km Dirasakan ,MMI IV-V Tanah Merah, IV-V Wamena, IV-V Merauke, II-III Jayapura '],
           ['2018-02-26', '00:52:11', 'WIB', 7.6,
            '266 km Tenggara BOVENDIGOEL-PAPUA, Kedlmn:96 Km, tdk berpotensi tsunami '],
           ['2018-02-26', '00:51:10', 'WIB', 7.6,
            '266 km Tenggara BOVENDIGOEL-PAPUA, Kedlmn:96 Km ']], dtype=object)
```

&nbsp;
Untuk code program dapat dilihat [disini](https://github.com/IanNarsa/iannarsa.github.io/blob/master/bmkg/bmkg.ipynb)

&nbsp;
&nbsp;
Previous Article :
&nbsp;
[#dirumahsaja emas naik](/)
Next Article :
&nbsp;
[Customer segmentation](/penjualan/supermarket_sale_analysis.html)