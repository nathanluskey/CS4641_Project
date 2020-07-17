from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas
import os
import pickle5 as pickle
import numpy as np
import pydotplus
import collections

def saveGraph(clf, filename, max_depth=None):
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
    #Initialize the tree
    #TODO: Impliment a pruned decision tree
    #Example: https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html#sphx-glr-download-auto-examples-tree-plot-cost-complexity-pruning-py
    
    ## Split data into train and test
    X_train, X_test, y_train, y_test = train_test_split(allFeatures, genreLabels, random_state=0)

    clf = DecisionTreeClassifier(criterion="entropy")

    #First look at alphas
    path = clf.cost_complexity_pruning_path(X_train, y_train)
    ccp_alphas, impurities = path.ccp_alphas, path.impurities
    #Train decision trees with the different ccp_alphas
    clfs = []
    for ccp_alpha in ccp_alphas:
        clf = DecisionTreeClassifier(random_state=0, ccp_alpha=ccp_alpha)
        clf.fit(X_train, y_train)
        clfs.append(clf)
    print("Number of nodes in the last tree is: {} with ccp_alpha: {}".format(
        clfs[-1].tree_.node_count, ccp_alphas[-1]))
    #Remove trivial case of 1 node
    clfs = clfs[:-1]
    ccp_alphas = ccp_alphas[:-1]
    #Compare accuracy on training and testing set
    train_scores = [clf.score(X_train, y_train) for clf in clfs]
    test_scores = [clf.score(X_test, y_test) for clf in clfs]

    fig, ax = plt.subplots()
    ax.set_xlabel("alpha")
    ax.set_ylabel("accuracy")
    ax.set_title("Accuracy vs alpha for training and testing sets")
    ax.plot(ccp_alphas, train_scores, marker='o', label="train",
            drawstyle="steps-post")
    ax.plot(ccp_alphas, test_scores, marker='o', label="test",
            drawstyle="steps-post")
    ax.legend()
    plt.show()
    plt.savefig("AlphaVSAccuracy.png")
    
    #TODO: Save and show the optimal tree
    if False:
        #From the graph take the max ccp_alpha training set
        print("Decision Tree Depth: {}".format(clf.get_depth()))
        #Save the tree by pickling the model for persistence
        with open("clf_pruned.pickle", "wb") as f:
            pickle.dump(clf, f)
        # Save a visualization of data
        filename = 'trainingOnMultipleFeatures_LargeTree_Pruned.png'
        saveGraph(clf, filename, max_depth=2)
        print("Tree saved to: \n\t{}".format(filename))