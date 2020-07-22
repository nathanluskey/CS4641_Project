'''
    Testing for K-means clustering of PCA reduced features
'''

import pandas
import os
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt


def find_optimal_num_clusters(title, X, max_K=10):
    iterationVals = np.arange(1,max_K+1)
    losses = []
    for i in range(1, max_K+1):
        # TODO: append losses here
        kmeans = KMeans(n_clusters=i).fit(X)
        kmeans.fit(X)
        losses.append(sum(np.min(cdist(X, kmeans.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])
    plt.plot(iterationVals, losses)
    plt.xlabel('k')
    plt.ylabel('Loss')
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    #np.set_printoptions(threshold=np.inf)
    parentDirectory = os.path.dirname(os.getcwd())
    path = os.path.join(parentDirectory, "SQLTesting", "compiledGenreData_AllAttributes_5000Songs.csv")
    file = pandas.read_csv(path)
    
    allFeatures = ["bars_confidence","bars_start", "beats_confidence","beats_start","danceability",
        "duration", "end_of_fade_in","energy","key","key_confidence","loudness","mode",
        "mode_confidence","sections_confidence","sections_start","segments_confidence",
        "segments_loudness_max","segments_loudness_max_time","segments_start","song_hotttnesss",
        "start_of_fade_out","tatums_confidence","tatums_start","tempo","time_signature",
        "time_signature_confidence"]
    X_all = file.loc[:,allFeatures].values
    X_all = np.nan_to_num(X_all)
    # Reduced to 10 features
    pca_all = PCA(n_components=10)
    principle_X_all = pca_all.fit_transform(X_all)
    print("X_all dim: ", principle_X_all.shape)

    features = ['year', 'tempo', 'duration', 'loudness', 'mode', 'key']
    X_some = file.loc[:,features].values
    X_some = np.nan_to_num(X_some)
    # Reduced to 2 features
    pca_some = PCA(n_components=3)
    principle_X_some = pca_some.fit_transform(X_some)
    print("X_some dim: ", principle_X_some.shape)
    
    find_optimal_num_clusters("Elbow Method with All Numerical Features",principle_X_all, max_K=15)
    find_optimal_num_clusters("Elbow Method with Important Numerical Features",principle_X_some, max_K=15)
    
    # The png's don't really show an obvious elbow, but k=6 for all features and k=8 for important features seems pretty good

