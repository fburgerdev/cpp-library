#!/bin/sh
# optional arguments
CONFIG=debug
TEST=test
while getopts "c:t:" opt; do
    case "${opt}" in
        c)
            CONFIG=${OPTARG};;
        t)
            TEST=${OPTARG};;
        *)
            exit;;
    esac
done

# premake -> make -> run test
premake5 gmake --file="build/premake5.lua" && make config=$CONFIG -C build && bin/${CONFIG}_${TEST}/${TEST}