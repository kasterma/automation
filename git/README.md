# learning git

## Subtree merging

https://nuclearsquid.com/writings/subtree-merging-and-you/

    mkdir A
    cd A
    git init .
    ~/projects/automation/git/create_some_commits.sh 10
    git log
    git adog
    cd ..
    mkdir B
    cd B
    git init .
    ~/projects/automation/git/create_some_commits.sh 10 file2.txt


    git merge -s ours --no-commit --allow-unrelated-histories projB/master
    git ss
    git read-tree --prefix=projB -u projB/master
    git ss
    git commit -m "Merge in projB into projB"

    ~/projects/automation/git/create_some_commits.sh 10 file.txt "Commit after IDX"
    git adog
    cd ..
    cd B
    ~/projects/automation/git/create_some_commits.sh 4 file2.txt "Commit B after IDX"
    cd ..
    cd A
    git fetch --all
    git adog
    git pull -s subtree projB master
