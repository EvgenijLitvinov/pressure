#!/usr/bin/env python3

from subprocess import call

with open('../pressure/flag.txt', 'r+') as fp:
    if fp.read(1) == '1':
        fp.seek(0)
        fp.write('0')
        call('wget -o log https://github.com/EvgenijLitvinov/pressure/archive/refs/heads/main.zip', shell=True)
        call('unzip main.zip -d main > log', shell=True)
call('./press.py')
