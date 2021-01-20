# -*- coding: utf-8 -*-
import pandas as pd 
import numpy as np

first = pd.read_pickle("customers_more_than_one_product.pkl")
data = pd.read_pickle("customers_more_than_one_product.pkl")

data['reviewerID'] = data["reviewerID"].rank(method='dense').astype(int)
data['asin'] = data["asin"].rank(method='dense').astype(int)
data['brand'] = data["brand"].rank(method='dense').astype(int)
data = data.drop(["reviewTime","reviewText","title"],1)

#tahminleme için örneklem sayısını 15000 belirledik
X= data["asin"].values[:15000]
x1=data["overall"].values[:15000]
x2=data["subjectivity"].values[:15000]
x3=data["polarity"].values[:15000]
X=np.vstack((X, x1,x2,x3)).T
