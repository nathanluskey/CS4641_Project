from sklearn import tree
import pandas
import os
import pickle5 as pickle

if __name__ == "__main__":
    #Read in the csv
    parentDirectory = os.path.dirname(os.getcwd())
    songFilehandle = os.path.join(parentDirectory, "SQLTesting", "compiledGenreData_AllAttributes_5000Songs.csv")
    pandas.read_csv(songFilehandle)

    #General info for tree here: https://scikit-learn.org/stable/modules/tree.html

    #TODO: Parse data for training the tree

    #TODO: Initialize the tree

    #TODO: Train the tree

    #TODO: Save the tree by pickling the model for persistence https://scikit-learn.org/stable/modules/model_persistence.html

    #TODO: Visualize the Tree