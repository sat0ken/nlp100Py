#!/usr/bin/env python3
# -*- coding: utf-8 -*-

col1 = []

with open("popular-names.txt") as f:
    lines = f.readlines()
    for line in lines:
        word = line.split("\t")
        col1.append(word[0].strip())

for i in sorted(set(col1)):
    print(i)
