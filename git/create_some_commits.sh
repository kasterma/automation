#!/usr/bin/env bash

if [[ $# -le 0 ]]; then
  echo "Call with number of commits to create"
  exit 1
fi

filename=${2:-"file.txt"}
message=${3:-"Commit message for commit IDX"}
contents=${4:-"commit commit IDX"}

for i in $(seq "$1"); do
  echo "${contents//IDX/$i}" >> "${filename}"
  git add ${filename}
  git commit -m "${message//IDX/$i}"
done
