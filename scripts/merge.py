from config import *
from files import *
from os import system

# include directory
create_directory(f'include/{config.project.lower()}')

# merge
origin = f'src/{config.project.lower()}.hpp'
dest = f'include/{config.project.lower()}/{config.project.lower()}.hpp'
default = 'src modules/*/include vendor/*/include'
ignore = 'modules/**.hpp vendor/**.hpp'
system(f'python3 {HPPMERGE}/hppmerge.py {origin} {dest} --default {default} --ignore {ignore}')