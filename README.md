# Data-Mining
DATA ANALYSIS OF AMAZON’S DATASET

Senem Yalın - Almira Gürkan

ABSTRACT

Data mining is the process of automatically discovering useful information in large
data repositories. We are drowning in data, but starving for knowledge. Natural language
processing (NLP) is an exciting branch of artificial intelligence (AI) that allows machines to
break down and understand human language. In this assignment, we used NLP techniques to
interpret text data that we are working with, for our analysis. In addition, Recommendation
System and Neural Network are used for prediction.

1-Introduction

This assignment has 7 steps which are Data Cleaning, Exploratory Data Analysis, Sentiment
Analysis, Text Generation, Regression, Neural Network Process, Recommendation Process. After
these steps, we had forward inferences.

2-Assignments

When we are doing text analysis part, we used several NLP libraries in Python including
TextBlob along with the standard machine learning libraries including pandas and scikit-learn.
We got results from the data which we analysed and plotted these results in many different ways.
Also we did Recommendation Analysis. After that, we printed the suggestions.

2.1 Data Pre-processing

2.1.1 Getting the data

We had 2 data sets, so we merged our data according to the columns that we will use. Our data
which we merged, has the columns below.
overall - rating of the product
reviewTime - time of the review (raw)
reviewerID - ID of the reviewer, e.g. A2SUAM1J3GNN3B
asin - ID of the product, e.g. 0000013714
reviewText - text of the review
title - name of the product
brand - brand name

2.1.2 Cleaning the data

We made text lowercase, removed punctuation and removed words containing numbers. Also
we got rid of some additional punctuation, non-sensical text that was missed the first time
around and stop words on ”reviewText” column.
