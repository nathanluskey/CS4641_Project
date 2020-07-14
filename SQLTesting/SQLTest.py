from MillionSongsApi import Api

# Test api
api = Api()
tracks = api.getTracks(10, offset=0)
print("Track Id:", tracks[0]['track_id'])
