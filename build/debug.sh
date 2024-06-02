#!/bin/sh
premake5 gmake --file="build/premake5.lua"
make --quiet -C build
bin/debug_test/test