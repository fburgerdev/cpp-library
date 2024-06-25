# PROJECT
>C++ library for ...

describe your project ...

DEPENDANCIES

## Usage
### Use Case 1
```cpp
    #include<iostream>

    int main() {
        std::cout << "Hello World!" << std::endl;
        return EXIT_SUCCESS;
    }
```

## Include this Library
In your c++ project
- add _include/PROJECTLOWERCASE_ to your include directories
- add _lib/[config]_ to your library directories (depending on your configuration)
- link the library _libPROJECTLOWERCASE.a_ (for linux) and _PROJECTLOWERCASE.lib_ (for windows)

INCLUDES

## Build (Optional)
#### Using Linux (Debian)
Locate the _build_ folder, then execute the following command in the console:
``` console
make config=[config]
```
If you have not installed _make_:
``` console
sudo apt-get install make -y
```

#### Using Windows
Open the _build/PROJECTLOWERCASE.sln_ solution with Visual Studio.

After selecting your desired configuration, click on _Build > Build Solution_.

__Note:__ Make sure you have the _Desktop developement with C++_ workload installed.