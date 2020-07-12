from doltpy.core import Dolt
import os
import sys


class Api:

    def __init__(self):
        self.path = os.path.join(os.getcwd(), 'million-songs')
        self.doltPath = os.path.join(self.path, '.dolt')
        self.repo = None

        if not os.path.isdir(self.doltPath):
            if os.path.isdir(self.path):
                try:
                    os.rmdir(self.path)
                except Exception as exc:
                    print("Exception:", exc)
                    print("Non-empty million-songs directory exists, but no .dolt file is present. "
                          "Delete the existing million-songs file.")
                    sys.exit()

            print("Initializing million-songs repository")
            self.repo = Dolt.clone('Liquidata/million-songs', '')
        else:
            self.repo = Dolt(repo_dir=self.path)

        self.trackAttributes = self.getTrackAttributes()


    def getTracks(self, count, offset=0):
        sql = "SELECT * FROM tracks LIMIT " + str(offset) + ", " + str(count)

        args = ['sql']
        args.extend(['--query', sql])
        tracks = self.repo.execute(args)
        startIndex = 3
        endIndex = len(tracks) - 2
        for i in range(startIndex, endIndex):
            track = tracks[i]
            trackAttributes = track.split('|')
            print("Track " + str(i))
            for tr in trackAttributes:
                print(tr)


    def getTrackAttributes(self):
        sql = "DESCRIBE tracks;"

        args = ['sql']
        args.extend(['--query', sql])
        attributes = self.repo.execute(args)
        startIndex = 3
        endIndex = len(attributes) - 2

        attributeList = {}

        for i in range(startIndex, endIndex):
            atrs = attributes[i].split('|')
            name = atrs[1].replace(' ','')
            type = atrs[2].replace(' ','')
            attributeList[name] = type

        return attributeList



