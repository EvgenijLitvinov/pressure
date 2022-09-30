#!/usr/bin/env python3

import os
from subprocess import call

print("Content-type: text/html\n")
print('''<!DOCTYPE HTML>
<html>
<head>
    <meta charset="utf-8">
    <title>Updater</title>
</head><body>''')

if os.path.exists('../pressure/flag.txt'):
    call('wget -o log https://github.com/EvgenijLitvinov/pressure/archive/refs/heads/main.zip', shell=True)
    call('unzip main.zip > log', shell=True)
    for file in os.listdir('pressure-main/root'):
        print(os.stat(file).st_mtime)
    print(os.stat('updater.py').st_mtime)
    print(os.stat('press.py').st_mtime)
#call('./press.py')

print('</body></html>')
