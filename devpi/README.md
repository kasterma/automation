# devpi

Get devpi set up for (initially) caching of data from pypi.

https://www.devpi.net/

pip install -i http://localhost:3141/root/pypi/+simple/ simplejson

In a requirements file can set it as follows:

    -i http://localhost:8989/root/pypi/+simple/
    -r requirements/requirements-base.txt
    -r requirements/requirements-testing.txt

(which also pulls in futher requirements files from the requirements directory).

## Requirements

The file `base-requirements.txt` contains the requirements as we have chosen them.  Then to get a stable install we
installed this into the docker and run pip freeze to get requirements.txt.  To refresh the requirements.txt (i.e. for
testing with newer versions) run `make freeze`.
