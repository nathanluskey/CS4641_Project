from sklearn import tree
import pandas
import os
import pickle5 as pickle
import numpy as np

if __name__ == "__main__":
    #Read in the csv
    parentDirectory = os.path.dirname(os.getcwd())
    songFilehandle = os.path.join(parentDirectory, "SQLTesting", "compiledGenreData_AllAttributes_5000Songs.csv")
    csv = pandas.read_csv(songFilehandle)

    #General info for tree here: https://scikit-learn.org/stable/modules/tree.html

    #TODO: Parse data for training the tree
    #Select the column headers with 'f' features
    # print(csv.columns) #To see all column headers
    #Can look at example on MSD for info: 
    importantFeatures = list(['artist_name', 'duration', 'energy', 'key', 'loudness', 
        'mode', 'end_of_fade_in', 'mode', 'song_hotttnesss', 'start_of_fade_out', 'tempo', 'time_signature', 'year'])
    allFeatures = np.empty(0)
    for featureTitle in importantFeatures:
        feature = csv[featureTitle]
        feature = np.array(feature)
        feature = feature.reshape((-1, 1))
        # print("Feature: {}, allFeatures.size = {}, feature.shape = {}, allFeatures.shape = {}".format(featureTitle, allFeatures.size, feature.shape, allFeatures.shape))
        if allFeatures.size == 0:
            #initialize it
            allFeatures = feature
        else:
            #stack onto it
            allFeatures = np.concatenate((allFeatures, feature), axis=1)
    #allFeatures is now an Nxf array with 'f' features and 'N' samples

    #Select the column of 'genre' for the labels
    genreLabel = csv['genre']
    
    #TODO: Initialize the tree

    #TODO: Train the tree

    #TODO: Save the tree by pickling the model for persistence https://scikit-learn.org/stable/modules/model_persistence.html

    #TODO: Visualize the Tree