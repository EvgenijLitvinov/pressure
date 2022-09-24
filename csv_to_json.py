#!/usr/bin/env python3
import json
# 26.06 - arr 1
# 23.09 - arr 2
FILE = '/media/jack/System/Users/HATAXA/Google Диск/pressure.csv'
data = {}

with open(FILE) as fd:
    for line in fd:
        line = line.strip().split(',')
        l = []
        for i in range(1, len(line), 3):
            l.append(dict(sys=line[i], dia=line[i+1], pul=line[i+2], arr=False))
        data[line[0]] = l

with open('data.json', 'w') as fp:
    json.dump(data, fp, indent=4)
