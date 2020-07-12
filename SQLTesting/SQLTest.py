from MillionSongsApi import Api
from doltpy.core import Dolt
import os
import sys

# Test api
api = Api()
print('Track attributes', api.getTrackAttributes())
print('Tracks', api.getTracks(count=10))
#api.repo.sql("SHOW TABLES;")
