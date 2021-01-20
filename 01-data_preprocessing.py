# -*- coding: utf-8 -*-


import pandas as pd

#Data preprocessing 
meta_all_beauty = pd.read_json('C:\\Users\\senem\\Desktop\\meta_All_Beauty.json',typ="frame",lines=True)

all_beauty = pd.read_json('C:\\Users\\senem\\Desktop\\All_Beauty.json',typ="frame",lines=True)

all_beauty_copy = all_beauty.drop(['verified','reviewerName','summary','unixReviewTime',
                                   'vote','style','image'], 1) #1 is for columns and 0 is for rows

#pickle it for later use
all_beauty_copy.to_pickle("all_beauty_second.pkl")


meta_all_beauty_copy = meta_all_beauty.drop(['category','tech1','fit','description','also_buy'
                                             ,'image','tech2','feature','rank','also_view','details'
                                             ,'main_cat','similar_item','date','price'], 1)


#if brand index is empty, this will remove that row 
meta_all_beauty_copy_not_null=meta_all_beauty_copy



for b, row in meta_all_beauty_copy.iterrows():  
    i=row['brand'] 
    if i == '':
        meta_all_beauty_copy_not_null= meta_all_beauty_copy_not_null.drop(b,0)
    
        
#pickle it for later use   
meta_all_beauty_copy_not_null.to_pickle("meta_all_beauty_not_null.pkl")


all_beauty_second = pd.read_pickle('all_beauty_second.pkl')
meta_all_beauty_not_null = pd.read_pickle('meta_all_beauty_not_null.pkl')

data_last = pd.merge(all_beauty_second,meta_all_beauty_not_null, how= 'right', on = 'asin')

data_last.to_pickle("data_last.pkl")


    
