import json, os

# name
workspace_config = json.load(open('cpp-library.json'))
header_name = workspace_config["project"].lower()

# merge
os.system(f'python3 cpp-library/modules/hppmerge/hppmerge.py src/{header_name}.hpp include/{header_name}/{header_name}.hpp src')