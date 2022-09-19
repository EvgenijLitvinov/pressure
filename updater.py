#!/usr/bin/env python3

from subprocess import call

with open('../pressure/flag.txt', 'r+') as fp:
    flag = fp.read()
    if flag:
        fp.write('\b0')
        call('curl -O https://github.com/EvgenijLitvinov/pressure/archive/refs/heads/main.zip', shell=True)
call('./press.py')

print("Content-type: text/html\n")
