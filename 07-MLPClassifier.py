# -*- coding: utf-8 -*-
import pandas as pd 
import numpy as np

first = pd.read_pickle("customers_more_than_one_product.pkl")
data = pd.read_pickle("customers_more_than_one_product.pkl")

data['reviewerID'] = data["reviewerID"].rank(method='dense').astype(int)
data['asin'] = data["asin"].rank(method='dense').astype(int)
