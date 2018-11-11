#!/usr/bin/env bash

docker exec -ti gitserver sh -c "create_repo $1.git"
git remote add local "ssh://git@localhost:2222/home/git/$1.git"