# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import pairwise_distances
import pandas as pd

data = pd.read_pickle("customers_more_than_one_product.pkl")
