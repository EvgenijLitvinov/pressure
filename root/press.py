#!/usr/bin/env python3

import sys, os, signal
import json, cgi
from datetime import datetime, timedelta
from time import time

if sys.argv[1]:
    os.kill(int(sys.argv[1]), signal.SIGTERM)

def bg_c(s, d):
    if s >= 180 or d >= 110:
        return 'DarkRed'
    if s >= 160 or d >= 100:
        return 'Red'
    if s >= 140 or d >= 90:
        return 'Salmon'
    if s >= 130 or d >= 85:
        return 'Orange'
    if s >= 120 or d >= 80:
        return 'Green'
    return 'Lime'

with open('../pressure/data.json') as fp:
    data = json.load(fp)

form = cgi.FieldStorage()
if form.getfirst('date'):
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

# -------------------- deletion -------------
if form.getfirst('del'):
    del_d = form.getfirst('del')[:-1]           # date
    del_n = int(form.getfirst('del')[-1])       # note
    data[del_d].pop(del_n)
    if len(data[del_d]) == 0:
        data.pop(data[del_d])

    with open('../pressure/data.json', 'w') as fp:
        json.dump(data, fp, indent=4)

# ------------------- last10 ---------------
#last10 = {}
#for key in list(data.keys())[-10:]:
#    last10[key] = data[key]


# ------------------ rendering ------------
print("Content-type: text/html\n")
print(f'''<!DOCTYPE HTML>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Heartbeat</title>
    <link rel="shortcut icon" href="../pressure/favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="../pressure/styles.css?{int(time())}"/>
    <link rel="stylesheet" href="../pressure/bootstrap.min.css"/>
    <script src="../pressure/bootstrap.bundle.min.js" defer></script>
    <script src="../pressure/scripts.js?{int(time())}" defer></script>
</head>
<body>
<dl>''')
for d in  list(data.keys())[-10:]:
    print(f'<dt>{d}:</dt>')
    for dd in data[d]:
        ddt = d + str(data[d].index(dd))
        print(f'''<dd>
            <button class="btn shadow" style="color: {bg_c(int(dd["sys"]), int(dd["dia"]))};" onclick="openDel(\'{ddt}\')">{dd["sys"]} / {dd["dia"]} - {dd["pul"]}  {dd["arr"]}</button>
            </dd>''')
    print(f'<script>window.scrollTo(0,document.body.scrollHeight);</script>')
print('</dl>')
# ------------------------- myDel ---------------------------------------
print(f'''
    <div id="myDel">
        <form method="post">
            <h3>Delete?</h3>
            <div class="btn-group">
                <button type="submit" class="btn btn-outline-dark" id="delBut">Yes</button>
                <button type="button" class="btn btn-outline-dark" onclick="closeDel()">No</button>
            </div>
        </form>
    </div>''')
# ------------------------ form modal witn button -------------------------------
ua_time = datetime.utcnow() + timedelta(hours=2)
print(f'''<button class="btn btn-success btn-lg" data-bs-toggle="modal" data-bs-target="#popup">
    ADDITION
</button>
<div class="modal fade" id="popup">
<div class="modal-dialog modal-sm"><form method="post">
    <div class="modal-content">
        <div class="modal-header">
            <div class="form-floating">
                <input type="date" class="form-control" name="date" placeholder="Date" value={ua_time.strftime('%Y-%m-%d')} required>
                <label for="date">Date</label>
            </div>
            <button class="btn-close mb-4" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
            <div class="d-flex justify-content-around mb-3">
                <div class="form-floating m-3">
                    <input id="myInput" type="number" class="form-control" name="sys" placeholder="120" required>
                    <label for="sys">SYS</label>
                </div>
                <div class="form-floating m-3">
                    <input type="number" class="form-control" name="dia" placeholder="80" required>
                    <label for="dia">DIA</label>
                </div>
            </div>
            <div class="d-flex justify-content-around">
                <div class="form-floating m-3">
                    <input type="number" class="form-control" name="pul" placeholder="60" required>
                    <label for="pul">Pulse</label>
                </div>
                <div class="form-check mt-4">
                    <input class="form-check-input" type="checkbox" id="arr" name="arr">
                    <label class="form-check-label" for="arr">Arrhythmia</label>
                    </div>                          
            </div>
        </div>
        <div class="modal-footer">
            <button type="submit" class="btn btn-primary">Save changes</button>
        </div>
    </div>
</form></div></div>
<script>window.scrollTo(0,document.body.scrollHeight);</script>
</body></html>''')
