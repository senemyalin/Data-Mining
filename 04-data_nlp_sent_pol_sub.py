# -*- coding: utf-8 -*-

from textblob import TextBlob
#on console > conda install -c conda-forge textblob
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_pickle('pre_clustering1.pkl')

pol = lambda x: TextBlob(x).sentiment.polarity
sub = lambda x: TextBlob(x).sentiment.subjectivity

data["reviewText"]= data["reviewText"].astype(str)

data['polarity'] = data['reviewText'].apply(pol)
data['subjectivity'] = data['reviewText'].apply(sub)

####yorumların polarity ve subjectivitylerini bulduk.
#polarity -1 ile 1 arasında, subjectivity 0 ile 1 arasında değişiyor.

data.to_pickle("data_nlp_sent_pol_sub.pkl")


#markaların polarity ve subjectivitylerini bularak 
#sitede bulunan markaların aldıkları yorumların 
#polarity ve subjectivitylerine baktık.

data = pd.read_pickle('data_nlp_sent_pol_sub.pkl')

pol=data.groupby('brand', as_index=False)['polarity'].mean()
sub=data.groupby('brand', as_index=False)['subjectivity'].mean()

brand_pol_sub = pd.merge(pol,sub, how= 'right', on = 'brand')

####Her markanın polarity ve subjectivitylerinin ortalamarını yazdırdık.
plt.figure()
fig, ax= plt.subplots(figsize=(8,4))

for index, brand in enumerate(brand_pol_sub.index):
    
    x = brand_pol_sub.loc[index,"polarity"]
    y = brand_pol_sub.loc[index,"subjectivity"]
    plt.scatter(x, y, color='blue')
    plt.text(x+.001, y+.001, brand_pol_sub['brand'][index], fontsize=10)
    
    
plt.title('Sentiment Analysis', fontsize=20)
plt.xlabel('<-- Negative -------- Positive -->', fontsize=15)
plt.ylabel('<-- Facts -------- Opinions -->', fontsize=15)

plt.savefig("pol_sub_brand_scatter.pdf")
plt.close(fig)


###5,4,3,2,1 puan alan marka sayılarını yazdırdık.
plt.figure()
fig, ax= plt.subplots(figsize=(8,4))

star=data.groupby('overall', as_index=False)['brand'].size()

star.plot.bar(x='overall',y='size', rot=0)
plt.xlabel('Overall', fontsize=15)
plt.ylabel('Brand', fontsize=15)

plt.savefig("rate_brand_barchart.pdf")
plt.close(fig)


###Genel olarak markaların 5 yıldız aldığını gördük ve 
#aynı zamanda markaların polarity ve subjectivitylerinin olumlu olduğunu gördük. 
#Karşılaştırmalarımız tutarlı ve başarılı.
