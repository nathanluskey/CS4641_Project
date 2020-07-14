import os
import pickle5 as pickle
import matplotlib.pyplot as plt
import numpy as np


def loadData():
    # Get the right directory
    parentDirectory = os.path.dirname(os.getcwd())
    SQLDirectory = "{}\\SQLTesting".format(parentDirectory)
    #Load the file
    with open("{}\\allData.pickle".format(SQLDirectory), "rb") as f:
        allData = pickle.load(f)
    return allData

if __name__ == "__main__":
    ## Load the fully compiled data
    allData = loadData()
    ## Get the genre labels & The tempo
    genreLabels = np.array(allData['genre'])
    tempos = np.array(allData['tempo'])
    uniqueGenreLabels = np.unique(genreLabels)
    # print(uniqueGenreLabels)
    #TODO: Create a box plot of variance of tempo across genre
    data = list()
    for genre in uniqueGenreLabels:
        booleanMask = genreLabels == genre
        genreTempos = tempos[booleanMask]
        data.append(genreTempos)
    
    print("plotting data")
    fig1, ax1 = plt.subplots()
    ax1.set_title('Basic Plot')
    ax1.boxplot(data)
    plt.boxplot(data, labels=uniqueGenreLabels)
    ax1.set_xticklabels(uniqueGenreLabels)
    plt.show()
    # fig1.savefig("data.png")