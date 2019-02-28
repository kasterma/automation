#!/Users/kasterma/projects/automation/convcommit/venv/bin/python
#
# example commit-mst that prints the result of the parsing
# rename to commit-msg, make executable, and place in .git/hooks/

import sys
from convc import extract

print(sys.argv)

with open(sys.argv[1], 'r') as commit_message_file:
    commit_msg = commit_message_file.read()

print(extract(commit_msg))
