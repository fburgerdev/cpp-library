# CPP-Library
> Python tool for C++ library developement

This project allows you to develop C++ libraries quickly and in a standartized manner.

## Usage
### Example Configuration
_MY_REPO/cpp-library.json_
```json
{
    "project": "MyProject",
    "author": "Florian Burger (@fburgerdev)",

    "libraries": [
        {
            "name": "math",
            "source": "https://github.com/fburgerdev/math"
        }
    ],
    "tests": {
        "test": {
            "files": [ "test.cpp" ]
        }
    }
}
```
### Setup Workspace
```console
cpp-library/setup
```
This will create the following files:
- _.vscode/c_cpp_properties.json_ (syncronized with project include directories)
- _.vscode/launch.json_ (debug configurations for every test specified in config)
- _include/merge.hpp_ (used by _hppmerge_ to automatically create single include header)
- _src/common.hpp_ (header file containing frequently used std includes)
- _LICENSE_ (MIT license, with author and year of creation)
- _README.md_ (basic structure, automatic dependancy listing)

### Run Tests
```console
cpp-library/setup [-t TEST_NAME] [-c CONFIG]
```

The following compilation steps take place:
- parse _cpp-library.json_ file and create _build/premake5.lua_
- execute _premake5_ on the newly created build script.
- run _MAKEFILE_
- executes test program

The single include header will be created by merging the headers in _include/merge.hpp_.

_Options:_
- _-t_ specifies the name of the test to be build, defaults to _test_
- _-c_ specifies the configuration to be used, defaults to _debug_

### Build
```console
cpp-library/build
```

Similarly to the _test_ script, the following compilation steps take place:
- parse _cpp-library.json_ file and create _build/premake5.lua_
- execute _premake5_ on the newly created build script.
- run _MAKEFILE_

Compilation will be repeated for all configurations (_debug_, _release_, _dist_).

The single include header will be created by merging the headers in _include/merge.hpp_.

### Clean
```console
cpp-library/clean
```
This command removes the following directories:
- _bin_
- _build_
- _lib_

## Include this Library
For an existing project, execute
```console
git submodule add git@github.com:fburgerdev/cpp-library.git
```
and for a new project, execute the following:
```console
git clone --recursive -b template git@github.com:fburgerdev/cpp-library.git
```