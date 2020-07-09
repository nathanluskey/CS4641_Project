import pickle5 as pickle

def parseTagtraumLine(inputString):
    trackID = line[:17]
    genre = line[19:-1]
    genre.replace("'", "")
    trackID.replace("'", "")
    return trackID, genre


if __name__ == "__main__":
    #For the tagtraum data
    tagtraum = open("MillionSongData/msd_tagtraum_cd2c.cls", "r")
    line = tagtraum.readline()
    i = 1
    # Impliment dictionary to store values with key = TRACKID, value = genre
    trackIDGenrePairs = dict()
    # Impliment a set to store all trackID and optimize searching if it's contained
    allTrackID = set()
    # for j in range(10): #Use this for quick testing
    while line != '':
        print("On Line: {}".format(i), end="\r")
        #First seven lines aren't useful
        #Example Line: 'TRZULQD128F1465697\tElectronic\n'
        if i > 7:
            trackID, genre = parseTagtraumLine(line)
            # add to dictionary
            trackIDGenrePairs[trackID] = genre
            # add to set
            allTrackID.add(trackID)
            #Check that things seem reasonable
            if i % 8000 == 0:
                print("track ID = {}, genre = {}".format(trackID, genre))
        i += 1
        line = tagtraum.readline()

    tagtraum.close
    # Use cPickle to store variables for dict and set
    with open("allTrackID.pickle", "wb") as f:
        pickle.dump(allTrackID, f)
    with open("trackIDGenrePairs.pickle", "wb") as f:
        pickle.dump(trackIDGenrePairs, f)
    #Example to Open file:
    # with open("allTrackID.pickle", "rb") as f:
    #     a = pickle.load(f)

    # #Tagtraum incorporates the topMAGD data, so no need to read it
    # topMAGD = False
    # if topMAGD:
    #     import requests
    #     # topMAGD = requests.get("https://www.w3schools.com/python/ref_requests_response.asp")
    #     print("Requesting Webpage", end="\r")
    #     topMAGD = requests.get("http://www.ifs.tuwien.ac.at/mir/msd/partitions/msd-MAGD-genreAssignment.cls")
    #     print("Webpage Loaded Successfully", end="\n")
    #     topMAGD = topMAGD.text #Returns a string of the webpage
    #     topMAGD = topMAGD.split("\n")
    #     print("Total Songs: {}".format(len(topMAGD)), end="\n")
    #     for i in range(10): #range(len(topMAGD)):
    #         print("Current Song: {}\r".format(i), end="\r")
    #         currentLine = topMAGD[i]
    #         #EXAMPLE LINE: TRAAAAK128F9318786\tPop_Rock
    #         trackID = currentLine[:17]
    #         genre = currentLine[19:]