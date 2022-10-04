#!/usr/bin/env python3

import filecmp
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
#    call('wget -o log https://github.com/EvgenijLitvinov/pressure/archive/refs/heads/main.zip', shell=True)
#    call('unzip main.zip > log', shell=True)
    if not filecmp.cmp('pressure-main/root/updater.py', 'updater.py', shallow=False):
        os.replace('pressure-main/root/updater.py', 'updater.py')
        print('<h5>update.py updated</h5>')
    if not filecmp.cmp('pressure-main/root/press.py', 'press.py', shallow=False):
        os.replace('pressure-main/root/press.py', 'press.py')
        print('<h5>press.py updated</h5>')
#call('./press.py')
print('DONE')

print('</body></html>')
