import pathlib, json, datetime, os

# paths
ROOT = "cpp-library"
TEMPLATES = "cpp-library/templates"

# config
workspace_config = json.load(open('cpp-library.json'))
if not "namespace" in workspace_config:
    workspace_config["namespace"] = workspace_config["project"]

# README.md
create_readme = True
if os.path.isfile("README.md"):
    reply = input("README already exists, should it be replaced? (y/n)")
    create_readme = reply.strip().lower().startswith('y')
if create_readme:
    with open("README.md", "w") as output:
        readme = open(f'{TEMPLATES}/README.md').read()
        readme = readme.replace("PROJECTLOWERCASE", workspace_config["project"].lower())
        readme = readme.replace("PROJECT", workspace_config["project"])
        readme = readme.replace("NAMESPACE", workspace_config["namespace"])
        if "libraries" in workspace_config and 0 < len(workspace_config["libraries"]):
            # dependancies
            dependancies = "## Dependancies"
            for library in workspace_config["libraries"]:
                dependancy = open(f'{TEMPLATES}/dependancy.md').read()
                dependancy = dependancy.replace("NAME", library["name"])
                dependancy = dependancy.replace("SOURCE", library["source"])
                dependancies += '\n'
                dependancies += dependancy
            readme = readme.replace("DEPENDANCIES", dependancies)
            # include
            includes = "In order to resolve the dependancies"
            for library in workspace_config["libraries"]:
                include = open(f'{TEMPLATES}/include.md').read()
                include = include.replace("NAME", library["name"])
                includes += '\n'
                includes += include
            readme = readme.replace("INCLUDES", includes)
        else:
            readme = readme.replace("DEPENDANCIES\n", "")
            readme = readme.replace("INCLUDES\n", "")
        output.write(readme)
# LICENSE
with open("LICENSE", "w") as output:
    license = open(f'{TEMPLATES}/LICENSE').read()
    license = license.replace("_AUTHOR_", workspace_config["author"])
    license = license.replace("_YEAR_", str(datetime.date.today().year))
    output.write(license)
# src/common.hpp
pathlib.Path("src").mkdir(parents=True, exist_ok=True)
with open("src/common.hpp", "w") as output:
    common = open(f'{TEMPLATES}/common.hpp').read()
    common = common.replace("NAMESPACE", workspace_config["namespace"])
    output.write(common)
# include/merge.hpp
if not os.path.isfile("include/merge.hpp"):
    pathlib.Path("include").mkdir(parents=True, exist_ok=True)
    with open("include/merge.hpp", "w") as output:
        merge = open(f'{TEMPLATES}/merge.hpp').read()
        output.write(merge)
# .vscode
pathlib.Path(".vscode").mkdir(parents=True, exist_ok=True)
# .vscode/c_cpp_properties.json
with open(".vscode/c_cpp_properties.json", "w") as output:
    properties = open(f'{TEMPLATES}/c_cpp_properties.json').read()
    output.write(properties)
# .vscode/c_cpp_properties.json
with open(".vscode/launch.json", "w") as output:
    launch = dict()
    launch["configurations"] = list()
    for test in workspace_config["tests"]:
        launch_config = open(f'{TEMPLATES}/launch.json').read()
        launch_config = launch_config.replace("TEST", test)
        launch["configurations"].append(json.loads(launch_config))
    output.write(json.dumps(launch, indent=4))