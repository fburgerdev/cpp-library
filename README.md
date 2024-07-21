# CPP-Library
> Python tool for C++ library developement

This project allows you to develop C++ libraries quickly and in a standartized manner.

The utility scripts _setup_, _test_, _build_ and _clean_ are currently only for linux.

## Usage
### Example Configuration
_MY_REPO/cpp-library.json_
```json
{
    "project": "project",
    "author": "florian burger (git@fburgerdev)",
    "namespace": "Project",

    "defines": [],
    "libraries": [
        { "name": "vecmath" },
        { "name": "beaver", "defines": [ "BEAVER_LOGGING "] }
    ],
    "tests": [
        { "name": "test", "files": [ "test.cpp", "other.cpp" ] }
    ]
}
```
### Setup
```console
cpp-library/setup
```
This will create the following files:
- _.vscode/c_cpp_properties.json_ (syncronized with project include directories)
- _.vscode/launch.json_ (debug configurations for specified and default tests)
- _src/[project].hpp_ (used by _hppmerge_ to automatically create single include header)
- _src/common.hpp_ and _src/common.cpp_ (precompiled header files containing frequently used std includes with aliases)
- _LICENSE_ (MIT license, with author and year of creation)
- _README.md_ (basic structure, automatic dependancy listing)

### Test
```console
cpp-library/test [-t TEST_NAME] [-c CONFIG]
```

The following compilation steps take place:
- parse _cpp-library.json_ file and create _build/premake5.lua_
- execute _premake5_ on the newly created build script.
- run _MAKEFILE_
- executes test program

The single include header will be created by merging the headers in _include/[project]/[project].hpp_.

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

The single include header will be created by merging the headers in _include/[project]/[project].hpp_.

### Clean
```console
cpp-library/clean
```
This command removes the following directories:
- _bin_
- _build_
- _include_
- _lib_

## Include this Library
For an existing project, execute
```console
git submodule add https://github.com/fburgerdev/cpp-library.git cpp-library
```
and for a new project, execute the following:
```console
git clone --recursive -b template https://github.com/fburgerdev/cpp-library.git newproject
cd newproject
git submodule update --remote --recursive cpp-library
```