import numpy as np
import csv
import tensorflow as tf
from tensorflow import keras


djia = []
news = []
with open('data/DJIA_table.csv', 'r') as infile:
    c = csv.reader(infile, quotechar='"')
    for line in c:
        djia.append(line)

with open('data/RedditNews.csv', 'r') as infile:
    c = csv.reader(infile, quotechar='"')
    for line in c:
        news.append(line)

# Data headers:
# djia  ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'] (1989,7)
# News  ['Date', 'News'] (73608,2), 25 headlines per date

# %%
print(news[0])
