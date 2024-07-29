from config import *
from files import *
from os import path
from datetime import date

# README.md
create_readme = True
# :: prompt
if path.isfile("README.md"):
    answer = input("README.md already exists, should it be replaced (y/n)?")
    create_readme = answer.strip().lower().startswith('y')
# :: create
if create_readme:
    with create_file("README.md") as output:
        source = read_file(f'{TEMPLATES}/README.md')
        source = source.replace("__PROJECT__", config.project)
        source = source.replace("__PROJECT_NAME__", config.project.lower())
        source = source.replace("__NAMESPACE__", config.namespace)
        if len(config.libraries) > 0:
            # dependancies
            dependancies = "## Dependancies"
            for library in config.libraries:
                dependancy = f'- {library.name}'
                # if library.url:
                #     dependancy += f', see {library.url}'
                dependancies += '\n'
                dependancies += dependancy
            source = source.replace("__DEPENDANCIES__", dependancies)
            # include
            includes = "In order to resolve the dependancies"
            for library in config.libraries:
                include = read_file(f'{TEMPLATES}/include.md')
                include = include.replace("__LIB_NAME__", library.name)
                includes += '\n'
                includes += include
            source = source.replace("__INCLUDES__", includes)
        else:
            source = source.replace("__DEPENDANCIES__\n", "")
            source = source.replace("__INCLUDES__\n", "")
        output.write(source)

# LICENSE
with create_file("LICENSE") as output:
    source = read_file(f'{TEMPLATES}/LICENSE')
    source = source.replace("__AUTHOR__", config.author)
    source = source.replace("__YEAR__", str(date.today().year))
    output.write(source)

# src/common.hpp
with create_file("src/common.hpp") as output:
    source = read_file(f'{TEMPLATES}/common.hpp')
    source = source.replace("__NAMESPACE__", config.namespace)
    output.write(source)

# src/common.cpp
with create_file("src/common.cpp") as output:
    output.write('#include "common.hpp"')

# src/PROJECT.hpp
if not path.isfile(f"src/{config.project.lower()}.hpp"):
    with create_file(f"src/{config.project.lower()}.hpp") as output:
        source = read_file(f'{TEMPLATES}/merge.hpp')
        output.write(source)

# .vscode
# :: .vscode/c_cpp_properties.json
with create_file(".vscode/c_cpp_properties.json") as output:
    source = read_file(f'{TEMPLATES}/c_cpp_properties.json')
    output.write(source)
# :: .vscode/c_cpp_properties.json
with create_file(".vscode/launch.json") as output:
    launch = dict()
    launch["configurations"] = list()
    for test in config.tests:
        launch_config = read_file(f'{TEMPLATES}/launch.json')
        launch_config = launch_config.replace("__TEST_NAME__", test.name)
        launch["configurations"].append(json.loads(launch_config))
    output.write(json.dumps(launch, indent=4))