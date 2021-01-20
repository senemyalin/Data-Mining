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

data3865 = data.copy()
for f, row in data3865.iterrows():
    brand=row['brand']
    if not (brand == 3865):
        data3865 = data3865.drop(f,0)
data3865 = data3865.drop('brand',1)

pol3865=data3865.groupby('reviewTime', as_index=False)['polarity'].mean()
sub3865=data3865.groupby('reviewTime', as_index=False)['subjectivity'].mean()
brand3865_pol_sub = pd.merge(pol3865,sub3865, how= 'right', on = 'reviewTime')
        
data4627 = data.copy()
for f, row in data4627.iterrows():
    brand=row['brand']
    if not (brand == 4627):
        data4627 = data4627.drop(f,0)
data4627 = data4627.drop('brand',1)

pol4627=data4627.groupby('reviewTime', as_index=False)['polarity'].mean()
sub4627=data4627.groupby('reviewTime', as_index=False)['subjectivity'].mean()
brand4627_pol_sub = pd.merge(pol4627,sub4627, how= 'right', on = 'reviewTime')

plt.figure()
fig, ax= plt.subplots(figsize=(8,4))

plt.plot(brand2839_pol_sub.reviewTime,brand2839_pol_sub.polarity, color='lightblue', label= "brand2839 polarity")
plt.plot(brand3865_pol_sub.reviewTime,brand3865_pol_sub.polarity, color='lightgreen', label= 'brand3865 polarity')
plt.plot(brand4627_pol_sub.reviewTime,brand4627_pol_sub.polarity, color='pink', label= 'brand4627 polarity')


plt.plot(brand2839_pol_sub.reviewTime,brand2839_pol_sub.subjectivity, color='blue', label= "brand2839 subjectivity")
plt.plot(brand3865_pol_sub.reviewTime,brand3865_pol_sub.subjectivity, color='green', label= 'brand3865 subjectivity')
plt.plot(brand4627_pol_sub.reviewTime,brand4627_pol_sub.subjectivity, color='purple', label= 'brand4627 subjectivity')

plt.xlabel("Year")
plt.ylabel("Polarity and Subjectivity")
plt.legend()
plt.title("Polarities and Subjectivities & Brand")


plt.savefig("Polarities and Subjectivities & Brand.pdf")
plt.close(fig)
