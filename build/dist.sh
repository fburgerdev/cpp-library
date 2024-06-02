#!/bin/sh
premake5 gmake --file="build/premake5.lua"
make config=debug -C build
make config=release -C build
make config=dist -C build
python3 build/hppmerge.py include/PROJECT_merge.hpp include/PROJECT.hpp src