Sigintwrapper
---------------


This is a simple wrapper which runs the provided program and
forwards SIGTERM to SIGINT.  This is because uWSGI listens for
SIGINT for restarts while runit sends SIGTERM.
