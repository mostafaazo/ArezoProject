#%%
import numpy as np
from sklearn.neighbors import BallTree
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
db = pd.read_csv("result7.csv")

#%%
distance_meter = 250
model = DBSCAN(eps=distance_meter / 111000,min_samples=2)
model.fit(db[['lat','long']].values)
lbl = model.labels_
db["cluster"] = lbl

#%%
plt.figure()
plt.scatter(db.long.values,db.lat.values,c=lbl)
plt.show()

#%%
db.to_csv("s.csv")

##