# -- coding: utf-8 --

import pandas as pd

data = pd.read_pickle('data_nlp_sent_pol_sub.pkl')

df = data.drop(['overall','reviewTime','reviewerID','title'], 1)

df["asin"]= df["asin"].astype(str)
#ürünlerin alınma sayılarına baktık.
#en fazla yorum alan yani en çok satılan üç ürün için wordcloud yapmaya karar verdik.
#Yorumlarda en çok kullanılan kelimeleri yazdırdık.
count = df.groupby('asin').size()

groupby_asin = count.to_frame('count').reset_index()

"""
ÜRÜNLER
B001QY8QXM
B00005JS5C
B000050FDY
"""
#üç ürünün bilgilerini ayırdık.
arr = ['B001QY8QXM','B00005JS5C','B000050FDY']
for f, row in df.iterrows():
    product=row['asin']

    if not(product in arr):
        df=df.drop(f,0)

df.to_pickle('choosen_products.pkl')


# Let's make some word clouds!
# Terminal / Anaconda Prompt: conda install -c conda-forge wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

data = pd.read_pickle('choosen_products.pkl')

# concatenate the string 
data = data.groupby(['brand'])['reviewText'].transform(lambda x : ' '.join(x))
data = data.drop_duplicates() 

df=pd.DataFrame(data,columns=['reviewText'])


df['reviewText']=df['reviewText'].str.split()


product1 = df.loc[2507,'reviewText']
product2 = df.loc[99745,'reviewText']
product3 = df.loc[8090,'reviewText']

product1_df = pd.DataFrame(product1,columns=['reviewText'])
product1_df = product1_df.groupby("reviewText").size().reset_index()

product2_df = pd.DataFrame(product2,columns=['reviewText'])
product2_df = product2_df.groupby("reviewText").size().reset_index()

product3_df = pd.DataFrame(product3,columns=['reviewText'])
product3_df = product3_df.groupby("reviewText").size().reset_index()


