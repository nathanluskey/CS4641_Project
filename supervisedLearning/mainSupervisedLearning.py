from sklearn import tree
import pandas
import os
import pickle5 as pickle
import numpy as np
import graphviz
import pydotplus
import collections


if __name__ == "__main__":
    #Read in the csv
    parentDirectory = os.path.dirname(os.getcwd())
    songFilehandle = os.path.join(parentDirectory, "SQLTesting", "compiledGenreData_AllAttributes_5000Songs.csv")
    csv = pandas.read_csv(songFilehandle)

    #General info for tree here: https://scikit-learn.org/stable/modules/tree.html

    ## Parse data for training the tree
    #Select the column headers with 'f' features
    # print(csv.columns) #To see all column headers
    #Can look at example on MSD for info: 
    # importantFeatures = list(['artist_name', 'duration', 'energy', 'key', 'loudness', 'mode', 'end_of_fade_in', 'mode', 'song_hotttnesss', 'start_of_fade_out', 'tempo', 'time_signature', 'year'])
    # TODO: For now just look at numerical data
    importantFeatures = list(['year', 'tempo', 'duration', 'loudness', 'mode', 'key'])
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
    genreLabels = np.array(csv['genre'])
    uniqueGenres = np.unique(genreLabels)
    #Initialize the tree
    #Documentation: https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier
    clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=0)
    #Train the tree
    clf = clf.fit(allFeatures, genreLabels)
    #Save the tree by pickling the model for persistence https://scikit-learn.org/stable/modules/model_persistence.html
    with open("clf.pickle", "wb") as f:
        pickle.dump(clf, f)
    #Visualize the Tree

    # Visualize data
    dot_data = tree.export_graphviz(clf,
                                    feature_names=importantFeatures,
                                    class_names=uniqueGenres,
                                    out_file=None,
                                    filled=True,
                                    rounded=True)
    #Using graphviz
    # graph = graphviz.Source(dot_data)
    # graph.render("trainingOnYear")
    
    
    #Using pydotplus
    graph = pydotplus.graph_from_dot_data(dot_data)
    nodes = graph.get_node_list()
    edges = graph.get_edge_list()

    #Create list of unique colors for each genre
    colors = ('red', 'green', 'blue', 'orange', 'yellow', 'fuchsia', 'green', 'lightseagreen', 'silver', 'coral', 'lightpink', 'mediumpurple','lightsteelblue','mediumvioletred','peachpuff','thistle')
    edges = collections.defaultdict(list)

    for node in nodes:
        if node.get_name() not in ('node', 'edge'):
            values = clf.tree_.value[int(node.get_name())][0]
            #color only nodes where only one class is present
            if max(values) == sum(values):    
                node.set_fillcolor(colors[np.argmax(values)])
            #mixed nodes get the default color
            else:
                node.set_fillcolor(colors[-1])

    graph.write_png('trainingOnMultipleFeatures.png')
    print("i, Colors, and Genre")

    for i in range(len(uniqueGenres)):
        print("\ti = {}, Color = {}, Genre = {}".format(i, colors[i], uniqueGenres[i]))
    