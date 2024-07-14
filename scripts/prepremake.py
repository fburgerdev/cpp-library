from config import *
from files import *
from sys import argv

# create_premake
def create_premake(test: Test | None) -> str:
    workspace = read_file(f'{TEMPLATES}/workspace.lua')
    workspace = workspace.replace('__PROJECT_NAME__', config.project)
    workspace = workspace.replace('__START_PROJECT__', test.name if test else config.project)
    # defines
    if len(config.defines):
        workspace = workspace.replace('__DEFINES__', '"' + '", "'.join(config.defines) + '"')
    else:
        workspace = workspace.replace('__DEFINES__', '')

    for current_test in [test] if test else config.tests:
        test_project = read_file(f'{TEMPLATES}/project_test.lua')
        test_project = test_project.replace('__PROJECT_NAME__', config.project)
        test_project = test_project.replace('__TEST_NAME__', current_test.name)
        # files
        for file in current_test.files:
            test_project = test_project.replace('__FILES__', 'ROOT .. "/tests/' + file + '", ' + '__FILES__')
        test_project = test_project.replace('__FILES__', '')
        # libraries
        for library in current_test.libraries:
            test_project = test_project.replace('__LINKS__', '"' + library.filename + '", ' + '__LINKS__')
        test_project = test_project.replace('__LINKS__', '')
        # defines
        if len(current_test.defines):
            test_project = test_project.replace('__DEFINES__', '"' + '", "'.join(current_test.defines) + '"')
        else:
            test_project = test_project.replace('__DEFINES__', '')
        workspace += '\n'
        workspace += test_project
    return workspace

# main
if __name__ == '__main__':
    source = create_premake(config.get_test(argv[1])) if len(argv) > 1 else create_premake(None)
    with create_file('build/premake5.lua') as output:
        output.write(source)