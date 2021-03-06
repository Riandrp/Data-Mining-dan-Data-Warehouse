# -*- coding: utf-8 -*-
"""tugasP7_2010511051.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aCo-P0l3EkxHNYZLnxg6jGxbzIJE-3NB

Nama : Riandra Putra Pratama

Nim : 2010511051

Kelas : Praktikum data mining dan data warehous B

# **TUGAS PERTEMUAN 6 : Decision Tree**

**Bangun Model Decision Tree, gunakan dataset hepatitis. Gunakan 70% record untuk digunakan untuk membangun model dan 30% record untuk menguji model.**
"""

import pandas as pd
csv_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/hepatitis/hepatitis.data'
headers=['Class', 'AGE', 'SEX', 'STEROID','ANTIVIRALS', 'FATIGUE', 'MALAISE','ANOREXIA', 'LIVER_BIG', 'LIVER_FIRM','SPLEEN_ALPABLE', 'SPIDERS', 'ASCITES', 'VARICES','BILIRUBIN', 'ALK PHOSPHATE', 'SGOT', 'ALBUMIN', 'PROTIME', 'HISTOLOGY']
df = pd.read_csv(csv_path, names = headers)

# Cek hasil import dan pemberian header
df.head()

"""# **Menidentifikasi dan menghandle missing value (Data Cleaning)**"""

# mengkonversi ? (tanda tanya) ke NaN
import numpy as np

# replace "?" to NaN
df.replace("?", np.nan, inplace = True)
df.head(5)

# mengidentifikasi missing value dengan isnull
missing_data = df.isnull()
missing_data.head()

# metode untuk menghitung true saja (jmlh missing value saja)
df.isnull().sum()

"""**Menangani Missing value**

<b>mereplace dengan mean untuk data numerical:</b>
<ul>
BILIRUBIN          6<br>
ALK PHOSPHATE     29<br>
SGOT               4<br>
ALBUMIN           16<br>
PROTIME           67<br>
</ul>
"""

# menghitung rata - rata BILIRUBIN kemudian mengganti NaN dengan rata - rata tersebut
avg_bili = df["BILIRUBIN"].astype("float").mean(axis=0)
df["BILIRUBIN"].replace(np.nan, avg_bili, inplace=True)
# menghitung rata - rata ALKPHOSPATE kemudian mengganti NaN dengan rata - rata tersebut
avg_alk = df["ALK PHOSPHATE"].astype("float").mean(axis=0)
df["ALK PHOSPHATE"].replace(np.nan, avg_alk, inplace=True)
# menghitung rata - rata SGOT kemudian mengganti NaN dengan rata - rata tersebut
avg_sgot = df["SGOT"].astype("float").mean(axis=0)
df["SGOT"].replace(np.nan, avg_sgot, inplace=True)
# menghitung rata - rata ALBUMIN kemudian mengganti NaN dengan rata - rata tersebut
avg_albu = df["ALBUMIN"].astype("float").mean(axis=0)
df["ALBUMIN"].replace(np.nan, avg_albu, inplace=True)
#menghitung rata - rata PROTIME kemudian mengganti NaN dengan rata - rata tersebut
avg_protime = df["PROTIME"].astype("float").mean(axis=0)
df["PROTIME"].replace(np.nan, avg_protime, inplace=True)

"""<b>mereplace dengan frequency (modus/yang paling sering muncul):</b> misal fitur dengan tipe kategorikal/boolean
<ul>
STEROID            1<br>
FATIGUE            1<br>
MALAISE            1<br>
ANOREXIA           1<br>
LIVER BIG         10<br>
LIVER FIRM        11<br>
SPLEEN ALPABLE     5<br>
SPIDERS            5<br>
ASCITES            5<br>
VARICES            5<br>
</ul>
"""

# menghitung nilai mana yang paling banyak pada kolom STEROID kemudian mereplace dengan nilai tersebut
VAL_STE=df['STEROID'].value_counts().idxmax()
df["STEROID"].replace(np.nan, VAL_STE, inplace=True)
# menghitung nilai mana yang paling banyak pada kolom FATIGUE kemudian mereplace dengan nilai tersebut
VAL_FAT=df['FATIGUE'].value_counts().idxmax()
df["FATIGUE"].replace(np.nan, VAL_FAT, inplace=True)
# menghitung nilai mana yang paling banyak pada kolom MALAISE kemudian mereplace dengan nilai tersebut
VAL_MAL=df['MALAISE'].value_counts().idxmax()
df["MALAISE"].replace(np.nan, VAL_MAL, inplace=True)
# menghitung nilai mana yang paling banyak pada kolom ANOREXIA kemudian mereplace dengan nilai tersebut
VAL_ANO=df['ANOREXIA'].value_counts().idxmax()
df["ANOREXIA"].replace(np.nan, VAL_ANO, inplace=True)
# menghitung nilai mana yang paling banyak pada kolom LIVER BIG kemudian mereplace dengan nilai tersebut
VAL_LIVB=df['LIVER_BIG'].value_counts().idxmax()
df["LIVER_BIG"].replace(np.nan, VAL_LIVB, inplace=True)
# menghitung nilai mana yang paling banyak pada kolom LIVER FIRM kemudian mereplace dengan nilai tersebut
VAL_LIVF=df['LIVER_FIRM'].value_counts().idxmax()
df["LIVER_FIRM"].replace(np.nan, VAL_LIVF, inplace=True)
# menghitung nilai mana yang paling banyak pada kolom SPLEEN ALPABLE kemudian mereplace dengan nilai tersebut
VAL_SPL=df['SPLEEN_ALPABLE'].value_counts().idxmax()
df["SPLEEN_ALPABLE"].replace(np.nan, VAL_SPL, inplace=True)
# menghitung nilai mana yang paling banyak pada kolom SPIDERS kemudian mereplace dengan nilai tersebut
VAL_SPI=df['SPIDERS'].value_counts().idxmax()
df["SPIDERS"].replace(np.nan, VAL_SPI, inplace=True)
# menghitung nilai mana yang paling banyak pada kolom ASCITES kemudian mereplace dengan nilai tersebut
VAL_ASC=df['ASCITES'].value_counts().idxmax()
df["ASCITES"].replace(np.nan, VAL_ASC, inplace=True)
# menghitung nilai mana yang paling banyak pada kolom VARICES kemudian mereplace dengan nilai tersebut
VAL_LIFB=df['VARICES'].value_counts().idxmax()
df["VARICES"].replace(np.nan, VAL_LIFB, inplace=True)

# mengecek apakah masih ada missing value atau tidak
df.isnull().sum()

# hasil keseluruhan tanpa missing value
df.head()

"""# **preprocessing**"""

from sklearn import preprocessing
le_ste=preprocessing.LabelEncoder()
le_fat=preprocessing.LabelEncoder()
le_mal=preprocessing.LabelEncoder()
le_ano=preprocessing.LabelEncoder()
le_livb=preprocessing.LabelEncoder()
le_livf=preprocessing.LabelEncoder()
le_sple=preprocessing.LabelEncoder()
le_spi=preprocessing.LabelEncoder()
le_asc=preprocessing.LabelEncoder()
le_var=preprocessing.LabelEncoder()

df['STEROID']=le_ste.fit_transform(df['STEROID'])
df['FATIGUE']=le_fat.fit_transform(df['FATIGUE'])
df['MALAISE']=le_mal.fit_transform(df['MALAISE'])
df['ANOREXIA']=le_ano.fit_transform(df['ANOREXIA'])
df['LIVER_BIG']=le_livb.fit_transform(df['LIVER_BIG'])
df['LIVER_FIRM']=le_livf.fit_transform(df['LIVER_FIRM'])
df['SPLEEN_ALPABLE']=le_sple.fit_transform(df['SPLEEN_ALPABLE'])
df['SPIDERS']=le_spi.fit_transform(df['SPIDERS'])
df['ASCITES']=le_asc.fit_transform(df['ASCITES'])
df['VARICES']=le_var.fit_transform(df['VARICES'])

# Hasil setelah dilakukan preprocessing
df.head()

"""# Penerapan Decision Tree"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

model_dtree = DecisionTreeClassifier()
X_train, X_test, y_train, y_test = train_test_split(df[['AGE', 'SEX' , 'STEROID', 'ANTIVIRALS', 'FATIGUE','MALAISE','ANOREXIA','LIVER_BIG','LIVER_FIRM','SPLEEN_ALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN', 'ALK PHOSPHATE', 'SGOT', 'ALBUMIN', 'PROTIME', 'HISTOLOGY']], df['Class'], test_size=0.3, random_state=0)
model_dtree.fit(X_train, y_train)

prediksi_dtree=model_dtree.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, prediksi_dtree)

# memvisualisasikan dengan grafik
from sklearn import tree
from sklearn.tree import export_text

tree.plot_tree(model_dtree.fit(df[['AGE', 'SEX', 'STEROID','ANTIVIRALS', 'FATIGUE', 'MALAISE','ANOREXIA', 'LIVER_BIG', 'LIVER_FIRM','SPLEEN_ALPABLE', 'SPIDERS', 'ASCITES', 'VARICES','BILIRUBIN', 'ALK PHOSPHATE', 'SGOT', 'ALBUMIN', 'PROTIME', 'HISTOLOGY']],df['Class']))
r = export_text(model_dtree,feature_names=['AGE', 'SEX', 'STEROID','ANTIVIRALS', 'FATIGUE', 'MALAISE','ANOREXIA', 'LIVER_BIG', 'LIVER_FIRM','SPLEEN_ALPABLE', 'SPIDERS', 'ASCITES', 'VARICES','BILIRUBIN', 'ALK PHOSPHATE', 'SGOT', 'ALBUMIN', 'PROTIME', 'HISTOLOGY'])
print(r)

#Menyimpan ke dalam bentuk png
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
import pydotplus
dot_data=StringIO()
export_graphviz(model_dtree, out_file=dot_data, filled= True, rounded=True, 
                special_characters=True, feature_names=['AGE', 'SEX', 'STEROID','ANTIVIRALS', 'FATIGUE', 'MALAISE','ANOREXIA', 'LIVER_BIG', 'LIVER_FIRM','SPLEEN_ALPABLE', 'SPIDERS', 'ASCITES', 'VARICES','BILIRUBIN', 'ALK PHOSPHATE', 'SGOT', 'ALBUMIN', 'PROTIME', 'HISTOLOGY'], class_names=['DIE','LIVE'])
graph=pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('hepatitis.png')