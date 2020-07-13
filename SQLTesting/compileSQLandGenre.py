from MillionSongsApi import Api
import os
import pickle5 as pickle
import pandas
import sys

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__



if __name__ == "__main__":
    #Using OS go to the approprpriate directory
    parentDirectory = os.path.dirname(os.getcwd())
    MillionSongDataDirectory = "{}\\MillionSongData".format(parentDirectory)
    #Load the set of all track id
    with open("{}/allTrackID.pickle".format(MillionSongDataDirectory), "rb") as f:
        trackIDSet = pickle.load(f)
    #Load the trackIDGenrePairs
    with open("{}/trackIDGenrePairs.pickle".format(MillionSongDataDirectory), "rb") as f:
        trackIDGenrePairs = pickle.load(f)
    #Start the millionsongDataAPI
    blockPrint() #To stop printing outputs
    databaseAPI = Api()
    #All Attributes in the API
    allTrackAttributes = ["track_id", "title", "artist_name", "artist_mbid", "artist_mbtags", "artist_mbtags_count", "artist_playmeid", "artist_terms", "artist_terms_freq", "artist_terms_weight", "audio_md5", "bars_confidence", "bars_start", "beats_confidence", "danceability", "duration", "end_of_fade_in", "energy", "key", "key_confidence", "loudness", "mode", "mode_confidence", "release", "release_7digitalid", "sections_confidence", "sections_start", "segments_confidence", "segments_loudness_max", "segments_loudness_max_time", "segments_loudness_start", "segments_pitches", "segments_start", "segments_timbre", "similar_artists", "song_hotttnesss", "song_id", "start_of_fade_out", "tatums_confidence", "tatums_start", "tempo", "time_signature", "time_signature_confidence", "track_7digitalid", "year"]
    allTrackAttributes.append("genre")
    #Create a pandas dataframe
    savedData = pandas.DataFrame(data=None)
    #TODO: Figure out the Number of entries in the database
    numEntries = 10
    #Loop through all tracks in database
    for i in range(numEntries):
        currentSong = databaseAPI.getTracks(1, offset=i)
        #Select the first element from the list
        currentSong = currentSong[0]
        #There's a space on the front and back of the track_id
        currentSong['track_id'] = currentSong['track_id'].replace(" ","")
        #Checking if trackID is in the set
        currentTrackID = currentSong['track_id']
        if currentTrackID in trackIDSet:
            enablePrint()
            print(currentTrackID)
            blockPrint()
            #TODO: For the current song, append the genre information
            currentGenre = trackIDGenrePairs[currentTrackID]
            #Add the data to the dataframe
            currentSong['genre'] = currentSong
            savedData = savedData.append(currentSong,ignore_index=True)
    #Save the dataframe as a csv
    savedData.to_csv("compiledGenreData_AllAttributes.csv")

            
