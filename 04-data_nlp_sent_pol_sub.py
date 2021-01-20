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

