from MillionSongsApi import Api
from doltpy.core import Dolt
import os
import sys

# Check if million songs exists
api = Api()
api.getTracks(count=50, offset=20)
api.repo.sql("SHOW TABLES;")
