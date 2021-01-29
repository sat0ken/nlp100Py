#!/usr/bin/env python3
# -*- coding: utf-8 -*-

col1 = []
col2 = []

def colwrite(path, data):
    with open(path, mode='w') as f:
        for col in data:
            f.write(col+"\n")

with open("popular-names.txt") as f:
    lines = f.readlines()
    for line in lines:
        word = line.split("\t")
        col1.append(word[0].strip())
        col2.append(word[3].strip())

colwrite("col1.txt", col1)
colwrite("col2.txt", col2)
