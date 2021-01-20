# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_pickle('data_nlp_sent_pol_sub.pkl')


df = data.drop(['overall','reviewerID','asin','reviewText','title'], 1)
######Polarity çıktılarından 3 marka seçtik. 
#Bu markaların yıllara göre yorum polarity ve subjectivity değişimlerini inceledik.
arr = [2839,4627,3865]
for f, row in df.iterrows():
    brand=row['brand']

    if not(brand in arr):
        df=df.drop(f,0)


df.to_pickle('choosen_brands.pkl')

data = pd.read_pickle('choosen_brands.pkl')  ###########

#data cleaning reviewTime
for f, row in data.iterrows():
    time=row['reviewTime']
    
    year=time.partition(',')[2]
    data.at[f, 'reviewTime'] = year

data["reviewTime"]= data["reviewTime"].astype(int)

data2839 = data.copy()
for f, row in data2839.iterrows():
    brand=row['brand']
    if not (brand == 2839):
        data2839 = data2839.drop(f,0)
data2839 = data2839.drop('brand',1)

pol2839=data2839.groupby('reviewTime', as_index=False)['polarity'].mean()
sub2839=data2839.groupby('reviewTime', as_index=False)['subjectivity'].mean()
brand2839_pol_sub = pd.merge(pol2839,sub2839, how= 'right', on = 'reviewTime')
      