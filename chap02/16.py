#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

read = sys.argv[1]

def filewrite(path, data):
    with open(path, mode='w') as f:
        for i in data:
            f.write(i)

with open("popular-names.txt") as f:
    data = f.readlines()
    num = len(data) / int(read)
    split = []

    for i in range(len(data)+1):
        if i != 0 and i % num == 0 or i == len(data):
            print(i)
            filewrite(str(i)+".txt", split)
            split = []
        else:
            split.append(data[i])

