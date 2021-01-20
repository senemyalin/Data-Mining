# -*- coding: utf-8 -*-

import pandas as pd

data_last_cleaned_reviewText = pd.read_pickle('data_last_cleaned_reviewText.pkl')

copy=data_last_cleaned_reviewText.copy()
sorted_copy = copy.sort_values('brand')

"""
random_number=0
first=""
for f, row in sorted_copy.iterrows():  
    i=row['brand'] 
    
    if(first == i):
        sorted_copy.at[f, 'brand'] = random_number
        
        
    elif(first !=i):
        first=i
        random_number= random_number +1
        sorted_copy.at[f, 'brand'] = random_number
"""
sorted_copy['brand'] = sorted_copy["brand"].rank(method='dense').astype(int)

sorted_copy.to_pickle("pre_clustering.pkl") #brandlere sayı atadık

count = sorted_copy.groupby('brand').size()

df = count.to_frame('count').reset_index()

#en üst ve en alt değerler çıkarılmaya başlandı
arr=[]
for f, row in df.iterrows():
    count=row['count'] 
    brand=row['brand'] 
    if (count < 51 or count>5000):
        arr.append(brand)
        
for f, row in sorted_copy.iterrows():  
    brand=row['brand']
    
    if (brand in arr):
        sorted_copy=sorted_copy.drop(f,0)
    
        
sorted_copy.to_pickle("pre_clustering1.pkl") #en üst ve en alt değerler çıkarıldı, ortalama değerler kaldı.


import matplotlib.pyplot as plt
last = pd.read_pickle('pre_clustering.pkl')

#üst ve alt değerlerin çıkarılmamış hali
count = last.groupby('brand').size()
df = count.to_frame('count').reset_index()


#üst ve alt değerlerin çıkarılmış hali
last1 = pd.read_pickle('pre_clustering1.pkl')

count1 = last1.groupby('brand').size()
df1 = count1.to_frame('count').reset_index()    


#plotting
fig, axs = plt.subplots(1,2)
fig.set_size_inches(12, 4)

df.plot.scatter(x ='brand', y='count',ax=axs[0])
df1.plot.scatter(x ='brand', y='count',ax=axs[1])

plt.savefig("groupby_brand.pdf")
plt.close(fig)
