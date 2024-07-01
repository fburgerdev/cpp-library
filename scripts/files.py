from pathlib import Path
from os import path

# directories
ROOT = f'{path.dirname(__file__)}/../'
TEMPLATES = f'{ROOT}/templates'
HPPMERGE = f'{ROOT}/modules/hppmerge'

# create_directory
def create_directory(dirpath: str):
    Path(dirpath).mkdir(parents=True, exist_ok=True)
# create_file
def create_file(filepath: str):
    create_directory(path.dirname(filepath))
    return open(filepath, "w")
# read_file
def read_file(filepath: str) -> str:
    return open(filepath, 'r').read()