'''
#_author_ : crossain
&File     ：find_build_py.py
&Date     : 2019/9/9
'''

import os


file_dir = os.path.dirname(__file__)
f1 = open('pynames',mode="w+")
for root, dirs, files in os.walk(file_dir):
    for file in files:
        name = file.split('.')
        if name[-1]=='py':
            f1.write(file)
            f1.write("\n")


f1.close()






