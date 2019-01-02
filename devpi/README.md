# devpi

Get devpi set up for (initially) caching of data from pypi.

https://www.devpi.net/

## Requirements

The file `base-requirements.txt` contains the requirements as we have chosen them.  Then to get a stable install we
installed this into the docker and run pip freeze to get requirements.txt.  To refresh the requirements.txt (i.e. for
testing with newer versions) run `make freeze`.