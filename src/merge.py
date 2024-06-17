import json, os

# name
workspace_config = json.load(open('cpp-library.json'))
name = workspace_config["project"]

# merge
os.system(f'python3 cpp-library/modules/hppmerge/hppmerge.py include/merge.hpp include/{name}.hpp src')