#!/usr/bin/env bash

docker exec -ti gitserver sh -c "create_repo data/$1.git"
git remote add local "ssh://git@gitserver:2222/home/git/data/$1.git"
