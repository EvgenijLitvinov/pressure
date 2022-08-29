#!/usr/bin/env python3

import json, cgi

with open('../pressure/data.json') as fp:
    data = json.load(fp)

# ------------------ rendering ------------
print("Content-type: text/html\n")
print('''<!DOCTYPE HTML>
<html>
<head>
    <meta charset="utf-8">
    <title>Heartbeat</title>
</head>
<body>
<dl>''')
for d in  data:
    print(f'<dt>{d}:</dt>')
    for dd in data[d]:
        print(f'<dd>{dd["sys"]} / {dd["dia"]} - {dd["pul"]}  {dd["arr"]}</dd>')
print('</dl></body></head>')
