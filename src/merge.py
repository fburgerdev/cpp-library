import json, os

# name
workspace_config = json.load(open('cpp-library.json'))
header_name = workspace_config["project"].lower()

# merge
os.system(f'python3 cpp-library/modules/hppmerge/hppmerge.py include/merge.hpp include/{header_name}.hpp src')