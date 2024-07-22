from config import *
from files import *
from sys import argv

# create_test_project
def create_test_project(test: Test) -> str:
    test_project = read_file(f'{TEMPLATES}/project_test.lua')
    
    # name
    test_project = test_project.replace('__TEST_NAME__', test.name)

    # files
    for file in test.files:
        test_project = test_project.replace('__FILES__', 'ROOT .. "/tests/' + file + '",\n      ' + '__FILES__')
    test_project = test_project.replace('__FILES__', '')

    # defines
    if len(test.defines):
        test_project = test_project.replace('__DEFINES__', '"' + '", "'.join(test.defines) + '"')
    else:
        test_project = test_project.replace('__DEFINES__', '')

    # libraries
    test_project = test_project.replace('__PROJECT_NAME__', config.project)
    for library in test.libraries:
        test_project = test_project.replace('__LINKS__', '"' + library.name + '", ' + '__LINKS__')
    test_project = test_project.replace('__LINKS__', '')

    return test_project
# create_premake
def create_premake(test: Test | None) -> str:
    workspace = read_file(f'{TEMPLATES}/workspace.lua')
    
    # name
    workspace = workspace.replace('__PROJECT_NAME__', config.project)

    # start project
    workspace = workspace.replace('__START_PROJECT__', test.name if test else config.project)

    # defines
    for define in config.defines:
        workspace = workspace.replace('__DEFINES__', f'"{define}", __DEFINES__')
    workspace = workspace.replace('__DEFINES__', '')

    # libraries
    for library in config.libraries:
        workspace = workspace.replace('__LINKS__', f'"{library.name}", __LINKS__')
    workspace = workspace.replace('__LINKS__', '')

    # tests
    if test:
        workspace += '\n' + create_test_project(test)
    else:
        for current_test in config.tests:
            workspace += '\n' + create_test_project(current_test)
    
    return workspace

# main
if __name__ == '__main__':
    source = create_premake(config.get_test(argv[1])) if len(argv) > 1 else create_premake(None)
    with create_file('build/premake5.lua') as output:
        output.write(source)