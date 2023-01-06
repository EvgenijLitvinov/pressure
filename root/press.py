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

def artm(arr):
    if arr:
        return '<img src="../pressure/artm.png" height="17" width="30">'
    else:
        return ''

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
more10 = int(form.getfirst("more")) if form.getfirst("more") else -10

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
<body>''')
# -------------------- more10 --------------------
print(f'''<form method="post">
<button name="more" value={more10 - 10}>
    <img src="../pressure/icon.jpeg" height="30" width="30">
</button></form>''')
# ------------------------------------------------
for d in  list(data.keys())[more10:]:
    print(f'''<div class="card text-bg-dark">
                <div class="card-header fw-bold">{d}</div>
                <div class="card-body ps-3">''')
    for dd in data[d]:
        ddt = d + str(data[d].index(dd))
        print(f'''<a class="btn" style="color: {bg_c(int(dd["sys"]), int(dd["dia"]))};"
                    onclick="openDel(\'{ddt}\')">
                    {dd["sys"]} / {dd["dia"]} &ensp; Пульс {dd["pul"]} &ensp;
                    &ensp; {artm(dd["arr"])}</a>''')
    print('</div></div>')
if not form.getfirst("more"):
    print(f'<script>window.scrollTo(0,document.body.scrollHeight);</script>')
# ------------------------- myDel ---------------------------------------
print(f'''
    <div id="myDel">
        <form>
            <button type="submit" class="btn btn-danger btn-lg mb-2" id="delBut">Удалить?</button>
            <button type="button" class="btn btn-outline-dark" onclick="closeDel()">Нет</button>
        </form>
    </div>''')
# ------------------------ form modal witn button -------------------------------
ua_time = datetime.utcnow() + timedelta(hours=2)
print(f'''<a class="Add" data-bs-toggle="modal" data-bs-target="#popup">
        <img src="../pressure/plus.png" height="100" width="100">
        </a>
<div class="modal fade" id="popup">
<div class="modal-dialog modal-sm"><form method="post">
    <div class="modal-content">
        <div class="modal-header">
            <input type="date" name="date" value={ua_time.strftime('%Y-%m-%d')} required>
            <button type="button" class="btn-close mb-4" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
            <label for="myInput">Давление:</label>
            <p>
                <input id="myInput" type="number" name="sys" placeholder="120" required>
            </p>
            <p>
                <input type="number" name="dia" placeholder="80" required>
            </p>
            <label for="pul">Пульс:</label>
            <p>
                <input type="number" name="pul" id="pul" placeholder="60" required>
            </p>
            <div class="form-check mt-4">
                <input class="form-check-input" type="checkbox" id="arr" name="arr">
                <label class="form-check-label" for="arr">Аритмия</label>
            </div>                          
        </div>
        <div class="modal-footer">
            <button type="submit" class="btn btn-secondary">Сохранить</button>
        </div>
    </div>
</form></div></div>''')
if not form.getfirst("more"):
    print('<script>window.scrollTo(0,document.body.scrollHeight);</script>')
print('</body></html>')
