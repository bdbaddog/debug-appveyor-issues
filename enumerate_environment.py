"""
Figure out paths in appveyor environment
"""
from __future__ import print_function
import os

def check_dir(path):
    """ enumerate files/directories under path"""
    print(r'-- Directories under %s'%path)
    for item in os.listdir(path):
        print("Path->%s"%os.path.join(path, item))


PATHDIRS = os.environ['PATH'].split(os.pathsep)
for p in PATHDIRS:
    print("Path->%s"%p)

check_dir('c:\\')
check_dir('C:/Program Files (x86)/')
check_dir('C:/Program Files/')
