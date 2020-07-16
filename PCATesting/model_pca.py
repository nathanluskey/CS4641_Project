'''
    Testing for K-means clustering of PCA reduced features
'''

import pandas
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

#np.set_printoptions(threshold=np.inf)
file = pandas.read_csv(".\SQLTesting\compiledGenreData_AllAttributes_5000songs.csv")
features = ["bars_confidence","bars_start", "beats_confidence","beats_start","danceability",
    "duration", "end_of_fade_in","energy","key","key_confidence","loudness","mode",
    "mode_confidence","sections_confidence","sections_start","segments_confidence",
    "segments_loudness_max","segments_loudness_max_time","segments_start","song_hotttnesss",
    "start_of_fade_out","tatums_confidence","tatums_start","tempo","time_signature",
    "time_signature_confidence"]
X = file.loc[:,features].values
# replacing NaN values; as far as I can tell, only prevalent in song_hotttnesss
X = np.nan_to_num(X)
Y = file.loc[:,["genre"]].values
# unsure what the ideal number of components is; should change later
pca = PCA(n_components=10)
principle_X = pca.fit_transform(X)
# unsure what the ideal number of clusters is; should change later
kmeans = KMeans(n_clusters=5)
kmeans.fit(principle_X)
print("dim reduced features: ", principle_X)

print("labels: ", kmeans.labels_)
