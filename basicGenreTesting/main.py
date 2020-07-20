import os
import matplotlib.pyplot as plt
import numpy as np
import pandas


def loadData():
    # Get the right directory
    parentDirectory = os.path.dirname(os.getcwd())
    SQLDirectory = "{}\\SQLTesting".format(parentDirectory)
    #Load the file
    csv = pandas.read_csv("{}\\compiledGenreData_AllAttributes_5000Songs.csv".format(SQLDirectory))
    return csv

if __name__ == "__main__":
    ## Load the fully compiled data
    allData = loadData()
    ## Get the genre labels & The tempo
    genreLabels = np.array(allData.loc[:, 'genre'])
    tempos = np.array(allData.loc[:, 'tempo'])
    uniqueGenreLabels = np.unique(genreLabels)
    # print(uniqueGenreLabels)
    # Create a box plot of variance of tempo across genre
    data = list()
    for genre in uniqueGenreLabels:
        booleanMask = genreLabels == genre
        genreTempos = tempos[booleanMask]
        data.append(genreTempos)
    
    print("Creating Boxplot")
    fig1, ax1 = plt.subplots()
    ax1.set_title('BPM vs. Genre')
    ax1.boxplot(data)
    plt.boxplot(data, labels=uniqueGenreLabels)
    ax1.set_xticklabels(uniqueGenreLabels)
    ax1.set(xlabel = "Genre", ylabel= "Beats per Minute (BPM)")
    fig1.savefig("BPMvsGenre_Boxplot.png")
    
    #Create a pi chart
    print("Creating Pie Graph")
    genreLengths = list()
    for songGenre in data:
        genreLengths.append(len(songGenre))
    fig1, ax1 = plt.subplots()
    ax1.pie(genreLengths, labels=uniqueGenreLabels, autopct="", startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    # ax1.set_title("Percentages of Genre")
    fig1.savefig("PieChartOfGenre.png")
    
    #Show both plots
    plt.show()