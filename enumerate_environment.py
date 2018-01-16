import os

pathdirs = os.environ.split(os.pathsep)
for p in pathdirs:
    print("Path->%s"%p)
    