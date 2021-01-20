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
