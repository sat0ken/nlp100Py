#!/usr/bin/env python3
# -*- coding: utf-8 -*-

col3 = {}

with open("popular-names.txt") as f:
    lines = f.readlines()
    sorted_col = sorted(lines, key=lambda x: int(x.split('\t')[2]), reverse=True)
    for line in sorted_col:
        print(line.strip())
        #word = line.split("\t")
        #col3[word[2].strip()] = word

#for i in sorted(col3, reverse=True):
#    print(col3[i])
