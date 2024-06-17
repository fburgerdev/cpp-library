import sys, pathlib, json

# parameters
test_name = sys.argv[1] if 1 < len(sys.argv) else None

# paths
ROOT = "cpp-library"
TEMPLATES = "cpp-library/templates"

# build/premake5.lua
pathlib.Path("build").mkdir(parents=True, exist_ok=True)
with open('build/premake5.lua', "w") as output:
    # config
    workspace_config = json.load(open('cpp-library.json'))
    if not "namespace" in workspace_config:
        workspace_config["namespace"] = workspace_config["project"]

    # workspace
    workspace_name = workspace_config["project"]
    workspace = open(f'{TEMPLATES}/workspace.lua').read()
    workspace = workspace.replace("WORKSPACE_NAME", workspace_name.lower())
    if test_name:
        workspace = workspace.replace("DEFAULT_TEST", test_name)
    else:
        workspace = workspace.replace("DEFAULT_TEST", workspace_name.lower())
    output.write(workspace)

    # test
    if test_name:
        test_config = workspace_config["tests"][test_name]
        # name
        test = open(f'{TEMPLATES}/test.lua').read()
        test = test.replace("TEST_NAME", test_name)
        test = test.replace("WORKSPACE_NAME", workspace_name.lower())
        # files
        for filename in test_config["files"]:
            token = "--[[ INSERT ADDITIONAL FILES HERE ]]"
            test = test.replace(token, 'ROOT .. "/tests/' + filename + '",\n\t\t' + token)
        # libraries
        if "libraries" in workspace_config:
            for library in workspace_config["libraries"]:
                token = "--[[ INSERT ADDITIONAL LINKS HERE ]]"
                test = test.replace(token, '"' + library["name"] + '", ' + token)
        if "libraries" in test_config:
            for library in test_config["libraries"]:
                token = "--[[ INSERT ADDITIONAL LINKS HERE ]]"
                test = test.replace(token, '"' + library["name"] + '", ' + token)
        output.write("\n")
        output.write(test)