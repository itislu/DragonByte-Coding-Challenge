#! /usr/bin/env bash

if [ -z "$1" ]; then
    solution_dir=$(pwd)
else
    solution_dir=${1%/}
fi
project_dir=$(dirname "$solution_dir")
solution_name=$(basename "$solution_dir")
outfile="$project_dir"/"$solution_name".zip

zip "$outfile" "$solution_dir"/solution.py "$project_dir"/utils/*.py
