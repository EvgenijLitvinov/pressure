#!/usr/bin/env python3

from subprocess import call
with open('flag.txt', 'r+') as fp:
    flag = fp.read()
    if flag:
        fp.write(0)
        call('wget https://github.com/EvgenijLitvinov/pressure/archive/refs/heads/main.zip', shell=True)
call('press.py')

print("Content-type: text/html\n")
