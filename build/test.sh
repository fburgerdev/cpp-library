#!/bin/sh
# CONFIG
if [ -z "$1" ]
then
    CONFIG=debug
else
    CONFIG=$1
fi

# premake -> make -> run test
premake5 gmake --file="build/premake5.lua" && make config=$CONFIG --quiet -C build && bin/${CONFIG}_test/test