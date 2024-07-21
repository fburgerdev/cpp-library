import json
import glob
from pathlib import Path
from files import *

# Library
class Library:
    # constructor
    def __init__(self, data: any) -> None:
        # name
        self.name = data['name']
        # description
        # self.description = data['description'] if 'description' in data else ''
        # defines
        self.defines :list[str] = data['defines'] if 'defines' in data else []
        # type
        # self.type = data['type'] if 'type' in data else 'static'
        # filename
        # self.filename = data['filename'] if 'filename' in data else self.name
        # url
        # self.url = data['url'] if 'url' in data else ''
# Test
class Test:
    # constructor
    def __init__(self, data: any, project_libraries: list[Library], project_defines: list[str]) -> None:
        # name
        self.name = data['name']
        # description
        # self.description = data['description'] if 'description' in data else ''
        # files
        self.files = data['files']
        # defines
        self.defines :list[str] = project_defines.copy()
        if 'defines' in data:
            for define in data['defines']:
                if not define in self.defines:
                    self.defines.append(define)
        # libraries
        self.libraries :list[Library] = project_libraries.copy()
        if 'libraries' in data:
            for library in data['libraries']:
                if not library in self.libraries:
                    self.libraries.append(Library(library))
# Config
class Config:
    # constructor
    def __init__(self) -> None:
        data = json.load(open('cpp-library.json'))
        # project
        self.project = data['project']
        # description
        # self.description = data['description'] if 'description' in data else ''
        # author
        self.author = ' '.join([word.capitalize() for word in data['author'].split(' ')]) if 'author' in data else 'Unknwon'
        # namespace
        self.namespace = data['namespace'] if 'namespace' in data else self.project
        # libraries
        self.libraries :list[Library]= []
        if 'libraries' in data:
            for library in data['libraries']:
                self.libraries.append(Library(library))
        # defines
        self.defines :list[str] = data['defines'] if 'defines' in data else []
        for library in self.libraries:
            self.defines += library.defines
        # test
        # :: tests
        self.tests :list[Test]= []
        if 'tests' in data:
            for test in data['tests']:
                self.tests.append(Test(test, self.libraries, self.defines))
        # :: default tests
        used_tests = []
        for test in self.tests:
            used_tests += [ Path(f'tests/{file}') for file in test.files ]
        for filepath in glob.iglob("tests/*.cpp"):
            path = Path(filepath)
            if path not in used_tests:
                test_name = path.name[0:path.name.find('.')]
                self.tests.append(Test({ "name": test_name, "files": [ path.name ] }, self.libraries, self.defines))
    # get_test
    def get_test(self, name: str) -> Test:
        for test in self.tests:
            if test.name == name:
                return test
        raise Exception(f'Test {name} not found')
# global
config = Config()