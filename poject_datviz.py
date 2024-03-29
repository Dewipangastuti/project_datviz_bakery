# -*- coding: utf-8 -*-
"""Projek_Datvis_Bakery.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tiMUv7XfvXvvrRro15ej_IwE8Qjj4cxG

# Import Library
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""# Read data"""

# menginput url lokasi penyimpanan data
data = "https://raw.githubusercontent.com/Ridwanridzi/Pacmann_Datvis/main/Bakery_Sales.csv"

# read data csv
bakery = pd.read_csv(data)

# melihat dataset teratas
bakery.head()

# menampilkan informasi data
bakery.info()

"""# Menampilkan presentase NaN"""

# menghitung jumlah persentase NaN terbanyak
percentage_nan = bakery.isna().sum().sort_values(ascending=False) / len(bakery) * 100

# menampilkan persentase NaN
percentage_nan

"""# Menghapus data dengan jumlah NaN 100%"""

# list kolom yang ingin dihapus
dropped = ["croque monsieur", "mad garlic"]

# menghapus kolom
bakery = bakery.drop(columns=dropped)

# menampilkan informasi data setelah menghapus kolom
bakery.info()

"""# Mengisi Missing Value dengan 0
hal ini dikarenakan pada beberapa kolom yang memilki missing value pada data ini bukanlah real missing value, akan tetapi maksudnya tidak dibeli
"""

# membuat list kolom menu
bakery_menu = [
    "angbutter",
    "plain bread",
    "jam",
    "americano",
    "croissant",
    "caffe latte",
    "tiramisu croissant",
    "cacao deep",
    "pain au chocolat",
    "almond croissant",
    "milk tea",
    "gateau chocolat",
    "pandoro",
    "cheese cake",
    "lemon ade",
    "orange pound",
    "wiener",
    "vanila latte",
    "berry ade",
    "tiramisu",
    "merinque cookies"
]

# membuat list kolom yang bukan menu
bakery_main = bakery[
    ["datetime",
    "day of week",
    "total",
    "place"]
]

#mengisi NaN dengan 0
bakery_filled = bakery[bakery_menu].fillna(0)

#check NaN
bakery_filled.isna().sum()

#check jumlah NaN
bakery_main.isna().sum()

"""# Merge data
Merge data utama dengan data yang sudah di isi missing valuenya
"""

# Merge bakery dan bakery_filled
merged_bakery = bakery_filled.combine_first(bakery)

# menyusun ulang kolom agar sesuai dengan kolom pada data bakery
merged_bakery = merged_bakery[bakery.columns]

# menampilkan data yang telah di merge
merged_bakery.head()

# melihat informasi data yang telah di merge
merged_bakery.info()

"""

# Mengisi data missing value pada kolom place dengan "unknown"
"""

# mengisi missing value pada kolom place
merged_bakery["place"].fillna("unknown", inplace=True)

# melihat informasi data yang telah di isi missing valuenya
merged_bakery.info()

"""# Drop data NaN pada kolom "datetime", "day of week",  dan "total"
"""

# menghilangkan baris NaN pada kolom "datetime", " day of week", dan "total"
bakery_clean = merged_bakery.dropna(subset=["datetime", "day of week", "total"])

# menghitung NaN dari data yang telah dibersihkan
bakery_clean.isna().sum()

# menampilkan deskripsi data yang sudah dibersihkan
bakery_clean.describe()

# menampilkan informasi data yang telah dibersihkan
bakery_clean.info()

"""# Menghapus data outlier pada kolom total yang lebih dari 1000000"""

# membuat boxplot untuk menampilkan outlier pada kolom total
sns.boxplot(data=bakery_clean, x="total")

# memilih data yang memiliki total kurang dari 1000000
bakery_final = bakery_clean[bakery_clean['total'] <= 1000000]

# menampilkan info data final
bakery_final.info()

# membuat boxplot untuk melihat outlier pada kolom total
sns.boxplot(data=bakery_final, x="total")

"""

# Menampilkan Data Clean dan Mengekspor Data

"""

# menampilan data hasil cleaning
bakery_final.head()

# mengeksport data menjadi CSV
bakery_final.to_csv('Bakery_Final.csv', index=False)
