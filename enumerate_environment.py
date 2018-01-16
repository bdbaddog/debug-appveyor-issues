import os

pathdirs = os.environ['PATH'].split(os.pathsep)
for p in pathdirs:
    print("Path->%s"%p)
