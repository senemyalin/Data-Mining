# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import pairwise_distances
import pandas as pd


data = pd.read_pickle("customers_more_than_one_product.pkl")
data = data.drop(['reviewTime','reviewText','brand','subjectivity'], 1)

data['reviewerID'] = data["reviewerID"].rank(method='dense').astype(int)
data['asin'] = data["asin"].rank(method='dense').astype(int)
data["overall"]= data["overall"].astype(int)


Mean = data.groupby(by="reviewerID",as_index=False)['overall'].mean()
Rating_avg = pd.merge(data,Mean,on='reviewerID')
Rating_avg['adg_rating'] = Rating_avg['overall_x']-Rating_avg['overall_y']

checking = pd.pivot_table(Rating_avg,values='overall_x',index='reviewerID',columns='asin')

last = pd.pivot_table(Rating_avg,values='adg_rating',index='reviewerID',columns='asin')


# Replacing NaN by Product(Asin) Average
final_product = last.fillna(last.mean(axis=0))

# Replacing NaN by user Average
final_customer = last.apply(lambda row: row.fillna(row.mean()), axis=1)

# customer similarity on replacing NAN by Customer(Reviewer) avg
a = cosine_similarity(final_customer)
np.fill_diagonal(a, 0 )
similarity_with_customer = pd.DataFrame(a,index=final_customer.index)
similarity_with_customer.columns=final_customer.index

# customer similarity on replacing NAN by Prdouct(Asin) avg
cos_sim = cosine_similarity(final_product)
np.fill_diagonal(cos_sim, 0 )
similarity_with_product = pd.DataFrame(cos_sim,index=final_product.index)
similarity_with_product.columns=final_product.index

def find_similar_customers(dataFrame,n):
    dataFrame = dataFrame.apply(lambda x: pd.Series(x.sort_values(ascending=False)
           .iloc[:n].index, 
          index=['top{}'.format(i) for i in range(1, n+1)]), axis=1)
    return dataFrame

# top 30 neighbours for each customer
sim_customer_30_c = find_similar_customers(similarity_with_customer,30)

# top 30 neighbours for each customer
sim_customer_30_p = find_similar_customers(similarity_with_product,30)

Rating_avg = Rating_avg.astype({"asin": str})
product_customer = Rating_avg.groupby(by = 'reviewerID')['asin'].apply(lambda x:','.join(x))

def customer_product_score(customer):
    product_bought_by_customer = checking.columns[checking[checking.index==customer].notna().any()].tolist()    
    customer_values = sim_customer_30_p[sim_customer_30_p.index==customer].values
    customer_values_list = customer_values.squeeze().tolist()
    is_in = product_customer[product_customer.index.isin(customer_values_list)]
    a = ','.join(is_in.values)
    product_bought_by_similar_customer = a.split(',')
    evaluated_product = list(set(product_bought_by_similar_customer)-set(list(map(str, product_bought_by_customer))))
    evaluated_product = list(map(int, evaluated_product))
    scores = []
    for product in evaluated_product:
        choosen_product = final_product.loc[:,product]
        is_in = choosen_product[choosen_product.index.isin(customer_values_list)]
        not_null = is_in[is_in.notnull()]
        avg_customer = Mean.loc[Mean['reviewerID'] == customer,'overall'].values[0]
        index = not_null.index.values.squeeze().tolist()
        correlated = similarity_with_product.loc[customer,index]
        f = pd.concat([not_null, correlated], axis=1)
        f.columns = ['adg_score','correlation']
        f['score']=f.apply(lambda x:x['adg_score'] * x['correlation'],axis=1)
        score_sum = f['score'].sum()
