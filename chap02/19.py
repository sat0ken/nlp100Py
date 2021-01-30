#!/usr/bin/env python3
# -*- coding: utf-8 -*-

col1 = {}

with open("popular-names.txt") as f:
    lines = f.readlines()
    for line in lines:
        words = line.split("\t")
        word = words[0].strip()
        if word in col1:
            col1[word] = col1[word]+1
        else:
            col1.setdefault(word, 1)

sorted_col1 = sorted(col1.items(), key = lambda x : x[1], reverse=True)

for i in sorted_col1:
    print(i[0], i[1])
