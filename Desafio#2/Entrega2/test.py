#Análise e manipulação de dados
import pandas as pd

#Visualização de dados
import matplotlib.pyplot as plt
import seaborn as sns

#Recursos estatísticos
from scipy import stats

#Vizualização geoespacial
import folium
from folium.plugins import HeatMap

#Analise de sentimento
from nltk.sentiment import SentimentIntensityAnalyzer

#DataFrames
train = pd.read_csv('X_trainCharlotte.csv')
trainReview = pd.read_csv('reviewsTestCharlotte.csv')

"""sia = SentimentIntensityAnalyzer()

for review in trainReview['text']:
    if(sia.polarity_scores(review)["compound"] > 0):
        trainReview.loc[trainReview["text"] == review, "IsPositive"] = 1
        #print(sia.polarity_scores(review)["compound"])
    else:
        trainReview.loc[trainReview["text"] == review, "IsPositive"] = -1
        #print(sia.polarity_scores(review)["compound"])

print(trainReview)
trainReview.to_csv('NEWTESTreviewsWithSentimentAnalysis.csv')"""

from sklearn.cluster import DBSCAN
dbscanConfig = DBSCAN(eps=0.001, min_samples=30)
dbscanResults = dbscanConfig.fit(train[["latitude","longitude"]])
print(dbscanResults.labels_)