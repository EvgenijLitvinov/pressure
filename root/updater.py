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

print('DONE')
if os.path.exists('../pressure/flag.txt'):
#    call('wget -o log https://github.com/EvgenijLitvinov/pressure/archive/refs/heads/main.zip', shell=True)
#    call('unzip main.zip > log', shell=True)
    zip_dir = 'pressure-main/root/'
    for file in os.listdir(zip_dir):
        if not filecmp.cmp(zip_dir+file, file, shallow=False):
            os.replace(zip_dir+file, file)
            print(f'<h5>{file} updated</h5>')
    zip_dir = 'pressure-main/pressure/'
    for file in os.listdir(zip_dir):
        if not filecmp.cmp(zip_dir+file, f'../pressure/{file}', shallow=False):
            os.replace(zip_dir+file, f'../pressure/{file}')
            print(f'<h5>{file} updated</h5>')            
#call('./press.py')

print('</body></html>')
