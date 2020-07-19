from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas
import os
import pickle5 as pickle
import numpy as np
import pydotplus
import collections

def plotImpurities(ccp_alphas, impurities, filename, showPlot=False, savePlot=True):
    fig, ax = plt.subplots()
    ax.plot(ccp_alphas[:-1], impurities[:-1], marker='o', drawstyle="steps-post")
    ax.set_xlabel("effective alpha")
    ax.set_ylabel("total impurity of leaves")
    ax.set_title("Total Impurity vs effective alpha for training set")
    if savePlot:
        plt.savefig(filename)
    if showPlot:
        plt.show()

def trainDecisionTrees(ccp_alphas,removeTrivial=True):
    clfs = []
    for ccp_alpha in ccp_alphas:
        clf = DecisionTreeClassifier(random_state=0, criterion="entropy",ccp_alpha=ccp_alpha)
        clf.fit(X_train, y_train)
        clfs.append(clf)
    print("Number of nodes in the last tree is: {} with ccp_alpha: {}".format(
        clfs[-1].tree_.node_count, ccp_alphas[-1]))
    #Remove trivial case of 1 node
    if removeTrivial:
        clfs = clfs[:-1]
        ccp_alphas = ccp_alphas[:-1]
    return clfs, ccp_alphas

def plotAccuracy(ccp_alphas, train_scores, test_scores, filename, savePlot=True, showPlot=True):
    #Plot
    fig, ax = plt.subplots()
    ax.set_xlabel("alpha")
    ax.set_ylabel("accuracy")
    ax.set_title("Accuracy vs alpha for training and testing sets")
    ax.plot(ccp_alphas, train_scores, marker='o', label="train",
            drawstyle="steps-post")
    ax.plot(ccp_alphas, test_scores, marker='o', label="test",
            drawstyle="steps-post")
    ax.legend()
    if savePlot:
        plt.savefig(filename)
    if showPlot:
        plt.show()


def saveGraph(clf, filename, max_depth=None):
# Can use max_depth to better visualize all data
    dot_data = export_graphviz(clf,
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
    #Do PCA
    features = ["bars_confidence","bars_start", "beats_confidence","beats_start","danceability",
    "duration", "end_of_fade_in","energy","key","key_confidence","loudness","mode",
    "mode_confidence","sections_confidence","sections_start","segments_confidence",
    "segments_loudness_max","segments_loudness_max_time","segments_start","song_hotttnesss",
    "start_of_fade_out","tatums_confidence","tatums_start","tempo","time_signature",
    "time_signature_confidence"]
    X = csv.loc[:,features].values
    #Deal with the NaN
    X = np.nan_to_num(X)
    # unsure what the ideal number of components is; should change later
    pca = PCA(n_components=10)
    principle_X = pca.fit_transform(X)

    #Getting the labels
    genreLabels = np.array(csv.loc[:, 'genre'])
    uniqueGenres = np.unique(genreLabels)
    
    # Pruned Decision TreeExample: 
    # https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html#sphx-glr-download-auto-examples-tree-plot-cost-complexity-pruning-py
    
    ## Split data into train and test
    X_train, X_test, y_train, y_test = train_test_split(principle_X, genreLabels, random_state=0)
    #Initiialize Tree
    clf = DecisionTreeClassifier(criterion="entropy")
    #Prune
    path = clf.cost_complexity_pruning_path(X_train, y_train)
    ccp_alphas, impurities = path.ccp_alphas, path.impurities
    
    #Compare impurities to alpha
    print("Plotting Impurities", end="\r")
    plotImpurities(ccp_alphas, impurities, "ImpuritiesVSAlpha_PCA.png", showPlot=False)
    print("Done plotting impurities", end="\n")
    
    #Train decision trees with the different ccp_alphas
    print("Training multiple decision trees", end="\r")
    clfs, ccp_alphas = trainDecisionTrees(ccp_alphas)
    print("Done training multiple decision trees", end="\n")

    #Compare accuracy on training and testing set
    train_scores = [clf.score(X_train, y_train) for clf in clfs]
    test_scores = [clf.score(X_test, y_test) for clf in clfs]
    
    #Show accuracy on test set and training set
    plotAccuracy(ccp_alphas, train_scores, test_scores, "AlphaVSAccuracy_PCA.png", showPlot=False)
    #Get the optimal ccp_alpha corresponding to the highest test score:
    optimal_ccp_alpha = ccp_alphas[np.where(test_scores == max(test_scores))[0][0]]
    optimal_clf = clfs[np.where(test_scores == max(test_scores))[0][0]]
    #Save the tree by pickling the model for persistence    
    print("optimal_ccp_alpha = {}".format(optimal_ccp_alpha))
    print("Optimal Decision Tree Depth = {}".format(optimal_clf.get_depth()))
    #Save the tree by pickling the model for persistence
    with open("optimal_clf_pruned_PCA.pickle", "wb") as f:
        pickle.dump(optimal_clf, f)
    # Save a visualization of data
    filename = "trainingOnMultipleFeatures_PCA_LargeTree_Pruned.png"
    saveGraph(optimal_clf, filename, max_depth=None)
    print("Tree saved to: \n\t{}".format(filename))