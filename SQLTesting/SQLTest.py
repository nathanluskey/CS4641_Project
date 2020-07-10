from doltpy.core import Dolt
from doltpy.core.write import bulk_import
from doltpy.core.read import read_table
import os

# Check if million songs exists
path = os.path.join(os.getcwd(),'million-songs')
doltPath = os.path.join(path,'.dolt')
repo = None
if not os.path.isdir(doltPath):
    print("Initializing million-songs repository")
    repo = Dolt.clone('Liquidata/million-songs','')
    print("Ready for query...")
else:
    repo = Dolt(repo_dir=path)
    print("Ready for query...")

print("Repository Directory:", repo.repo_dir())
print(repo.sql(query="SHOW TABLES;"))
