# -*- coding: utf-8 -*-

import pandas as pd

data_last = pd.read_pickle('data_last.pkl')

reviewText = data_last.loc[:,'reviewText']


def clean_text_round1(text):
    '''Make text lowercase, remove punctuation and remove words containing numbers.'''
    text = text.str.lower()
    text = text.str.replace('[^\w\s]','')
    text = text.str.replace('\w*\d\w*', '')
    return text

reviewText_cleaned = clean_text_round1(reviewText)

def clean_text_round2(text):
    '''Get rid of some additional punctuation and non-sensical text that was missed the first time around.'''
    text = text.str.replace('[‘’“”…_]', '')
    text = text.str.replace('\n', '')
    return text

reviewText_cleaned = clean_text_round2(reviewText_cleaned)

reviewText_cleaned_df = reviewText_cleaned.to_frame()
data_last['reviewText'] = reviewText_cleaned_df['reviewText']


from sklearn.feature_extraction import text
stop = text.ENGLISH_STOP_WORDS

pat = r'\b(?:{})\b'.format('|'.join(stop))
data_last['reviewText'] = data_last['reviewText'].str.replace(pat,'')
data_last['reviewText'] = data_last['reviewText'].str.replace(r'\s+',' ')

for a, row in data_last.iterrows():  
    i=row['reviewText'] 
    if i == '' or i =='                   g' or i == '                       ' or i == '   ' or i==' ' :
        data_last= data_last.drop(a,0)


data_last.to_pickle("data_last_cleaned_reviewText.pkl")
