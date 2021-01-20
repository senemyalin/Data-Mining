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
