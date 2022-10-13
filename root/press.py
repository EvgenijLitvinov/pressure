#!/usr/bin/env python3

import sys, os, signal
import json, cgi
from datetime import datetime

os.kill(int(sys.argv[1]), signal.SIGTERM)

with open('../pressure/data.json') as fp:
    data = json.load(fp)

form = cgi.FieldStorage()
if form:
    date = datetime.strptime(form.getfirst('date'), '%Y-%m-%d')
    date = date.strftime('%d.%m.%y')

    small_dict = {'sys': form.getfirst('sys'),
                'dia': form.getfirst('dia'),
                'pul': form.getfirst('pul'),
                'arr': True if form.getfirst('arr') else False}
    
    if data.get(date):
        data[date].append(small_dict)
    else:
        data[date] = [small_dict]

    with open('../pressure/data.json', 'w') as fp:
        json.dump(data, fp, indent=4)

# ------------------ rendering ------------
print("Content-type: text/html\n")
print('''<!DOCTYPE HTML>
<html>
<head>
    <meta charset="utf-8">
    <title>Heartbeat</title>
    <link rel="stylesheet" href="pressure/styles.css"/>
    <link rel="shortcut icon" href="../pressure/favicon.ico" type="image/x-icon">
    <script src="../pressure/formscript.js" defer></script>
</head>
<body>
<dl>''')
for d in  data:
    print(f'<dt>{d}:</dt>')
    for dd in data[d]:
        print(f'<dd>{dd["sys"]} / {dd["dia"]} - {dd["pul"]}  {dd["arr"]}</dd>')
print(f'''</dl>
<button onclick="openForm()">Add</button>
<div id="myForm">
  <form>
    <h1>Enter</h1>

    <label for="date"><b>Date</b></label>
    <input type="date" name="date" required>

    <label for="sys"><b>SYS</b></label>
    <input type="number" placeholder="120" name="sys" required>

    <label for="dia"><b>DIA</b></label>
    <input type="number" placeholder="80" name="dia" required>

    <label for="pul"><b>Pulse</b></label>
    <input type="number" placeholder="60" name="pul" required>

    <label for="arr"><b>Arrhythmia</b></label>
    <input type="checkbox" name="arr">    

    <button type="submit">Add again</button>
    <button type="button" onclick="closeForm()">Close</button>
  </form>
</div>
</body></html>''')
