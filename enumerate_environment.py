from __future__ import print_function
import os

def check_dir(path):
    print(r'-- Directories under %s'%path)
    for p in os.listdir(path):
        print("Path->%s"%p)


pathdirs = os.environ['PATH'].split(os.pathsep)
for p in pathdirs:
    print("Path->%s"%p)

check_dir('c:\\')
check_dir('C:/Program Files (x86)/')
check_dir('C:/Program Files/')
