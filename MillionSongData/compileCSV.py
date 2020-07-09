import pandas
import pickle5 as pickle

if __name__ == "__main__":
    #Load the allTrackID
    with open("MillionSongData/allTrackID.pickle", "rb") as f:
        trackIDSet = pickle.load(f)
    #Load the trackIDGenrePairs
    with open("MillionSongData/trackIDGenrePairs.pickle", "rb") as f:
        trackIDGenrePairs = pickle.load(f)
    # read the CSV
    abridgedCSV = pandas.read_csv("MillionSongData/subset-compiled.csv")
    # print(abridgedCSV.columns)
    # Column is: 'track_id'
    newColumns = abridgedCSV.columns
    newCSV = pandas.DataFrame()
    #Go through each row of the old csv
    for i in range(abridgedCSV.shape[0]):
    # for i in range(10): #For quick testing
        print("On row: {}".format(i), end="\r")
        abridgedCSVTrackID = abridgedCSV['track_id'][i]
        abridgedCSVTrackID = abridgedCSVTrackID[2:-1]
        # print(repr(abridgedCSVTrackID))
        #Check if value is in the set
        if (abridgedCSVTrackID in trackIDSet):
            #Print a few to get a good idea that  it's working
            if i % 8000 < 10:
                print("track_id = {0}, row = {1}".format(abridgedCSVTrackID, i+1))
            currentRow = abridgedCSV[i:i+1]
            currentGenre = trackIDGenrePairs[abridgedCSVTrackID]
            #Append genre to current row
            currentRow['genre'] = currentGenre
            #Append row to newCSV
            newCSV = newCSV.append(currentRow)

    # Write CSV File
    newCSV.to_csv("compiledGenreData_MissingAttributes.csv")