#!/usr/bin/env python3

import shutil
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
    call('wget -o log https://github.com/EvgenijLitvinov/pressure/archive/refs/heads/main.zip', shell=True)
    call('unzip main.zip > log', shell=True)
    zip_dir = 'pressure-main/root/'
    for file in os.listdir(zip_dir):
        if not filecmp.cmp(zip_dir+file, file, shallow=False):
            os.replace(zip_dir+file, file)
            os.chmod(file, 0o700)
    zip_dir = 'pressure-main/pressure/'
    for file in os.listdir(zip_dir):
        if file not in os.listdir('../pressure/') or not filecmp.cmp(zip_dir+file, f'../pressure/{file}', shallow=False):
            os.replace(zip_dir+file, f'../pressure/{file}')
    for file in ['log', 'main.zip', '../pressure/flag.txt']:
        os.chmod(file, 0o602)
        os.remove(file)
    shutil.rmtree('pressure-main', ignore_errors=True)

call('./press.py')

print('</body></html>')
