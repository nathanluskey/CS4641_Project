from doltpy.core import Dolt
import os
import sys

# Check if million songs exists
path = os.path.join(os.getcwd(), 'million-songs')
doltPath = os.path.join(path, '.dolt')
repo = None
if not os.path.isdir(doltPath):
    if os.path.isdir(path):
        try:
            os.rmdir(path)
        except Exception as exc:
            print("Exception:", exc)
            print("Non-empty million-songs directory exists, but no .dolt file is present. "
                  "Delete the existing million-songs file.")
            sys.exit()

    print("Initializing million-songs repository")
    repo = Dolt.clone('Liquidata/million-songs', '')
else:
    repo = Dolt(repo_dir=path)

print("Ready for query...")
print("Repository Directory:", repo.repo_dir())
print(repo.sql(query="SHOW TABLES;"))
