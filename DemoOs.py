# DemoOs.py

from os.path import *

filename = "python.exe"
print(abspath(filename))
print(basename("c:\\work\\demo.txt"))

if exists("c:\\python310\\python.exe"):
    print("파일크기:{0}".format(getsize("c:\\python310\\python.exe")))
else:
    print("파일이 없습니다.")

import os
print("운영체제이름:{0}".format(os.name))
print("환경변수:{0}".format(os.environ))
os.system("notepad.exe")

import glob
print(glob.glob("c:\\work\\*.py"))