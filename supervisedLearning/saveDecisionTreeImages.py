from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas
import os
import pickle5 as pickle
import numpy as np
import pydotplus
import collections

def saveGraph(clf, filename, max_depth=None, suppressPrinting=False):
# Can use max_depth to better visualize all data
    dot_data = export_graphviz(clf,
                                feature_names=importantFeatures,
                                class_names=uniqueGenres,
                                max_depth=max_depth,
                                out_file=None,
                                filled=True,
                                rounded=True)
    
    
    #Using pydotplus
    graph = pydotplus.graph_from_dot_data(dot_data)
    nodes = graph.get_node_list()

    #Create list of unique colors for each genre
    colors = ('red', 'green', 'blue', 'orange', 'yellow', 'fuchsia', 'green', 'lightseagreen', 'silver', 'coral', 'lightpink', 'mediumpurple','lightsteelblue','mediumvioletred','peachpuff','thistle', 'white')

    for node in nodes:
        if node.get_name() not in ('node', 'edge'):
            values = clf.tree_.value[int(node.get_name())][0]
            #color only nodes where only one class is present
            if max(values) == sum(values):    
                node.set_fillcolor(colors[np.argmax(values)])
            #mixed nodes get the default color
            else:
                #If not a leaf node, color white
                node.set_fillcolor(colors[-1])

    graph.write_png(filename)
    if (not suppressPrinting):
        print("i, Colors, and Genre")
        for i in range(len(uniqueGenres)):
            print("\ti = {}, Color = {}, Genre = {}".format(i, colors[i], uniqueGenres[i]))

if __name__ == "__main__":
    #Read in the csv, assuming starting on the most local directory
    parentDirectory = os.path.dirname(os.getcwd())
    songFilehandle = os.path.join(parentDirectory, "SQLTesting", "compiledGenreData_AllAttributes_5000Songs.csv")
    csv = pandas.read_csv(songFilehandle)
    #General info for tree here: https://scikit-learn.org/stable/modules/tree.html

    ## Parse data for training the tree
    importantFeatures = ['year', 'tempo', 'duration', 'loudness', 'mode', 'key']
    allFeatures = np.array(csv.loc[:, importantFeatures].values)
    genreLabels = np.array(csv.loc[:, 'genre'])
    uniqueGenres = np.unique(genreLabels)

    #Load the Graph
    with open("optimal_clf_pruned.pickle", "rb") as f:
        optimal_clf = pickle.load(f)
    
    #Create a new directory
    try:
        os.mkdir("AllDecisionTrees")
    except:
        print("Directory already exists")
    #Switch to new directory
    os.chdir(os.path.join(os.getcwd(), "AllDecisionTrees"))
    for i in range(optimal_clf.get_depth()):
        i = i + 1
        print("Making graph for n={}".format(i), end="\r")
        filename = "n={}_OptimalDecisionTree.png".format(i)
        saveGraph(optimal_clf, filename, max_depth=i, suppressPrinting = True)

    