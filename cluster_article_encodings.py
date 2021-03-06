# -*- coding: utf-8 -*-
"""cluster_article_encodings.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zGrq9tV0-cAQMNwSDDGMe89qhcTazP2j
"""

#Function cluster_article_encodings - clusters article sentences encoding to ceiling of the sqrt of the number of article sentences
# and returns the sentences that are closest to the centroid of each cluster
def cluster_article_encodings(article_sentences, article_encodings, n=3):
  #KMeans clustering
  from sklearn.cluster import KMeans
  from sklearn.metrics import pairwise_distances_argmin_min

  #Sentence tokenization
  import nltk
  from nltk.tokenize import sent_tokenize
  nltk.download('punkt')

  from tqdm import tqdm, trange
  import pandas as pd
  import io
  import numpy as np
  import matplotlib.pyplot as plt

  n_clusters = int(np.ceil(len(article_sentences)**0.5))
  print(n_clusters)
  kmeans = KMeans(n_clusters=n_clusters, random_state=0)
  kmeans = kmeans.fit(article_encodings)
  y_kmeans = kmeans.predict(article_encodings)
  print(y_kmeans)
  avg = []
  closest = []
  for j in range(n_clusters):
    idx = np.where(kmeans.labels_ == j)[0]
    avg.append(np.mean(idx))
  closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, article_encodings)
  ordering = sorted(range(n_clusters), key=lambda k: avg[k])
  summary = '\n'.join([article_sentences[closest[idx]] for idx in ordering])
  print(summary)
  return kmeans, y_kmeans, summary