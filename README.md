Sigintwrapper
---------------

This is a simple wrapper which runs the provided program and
forwards SIGTERM to SIGINT.  This is because uWSGI listens for
SIGINT for restarts while runit sends SIGTERM.


Usage
---------------

After installing via:

    pip install sigintwrapper

Use via:

    sigintwrapper /absolute/path/to/program [with arguments]
