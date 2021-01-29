#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

read = sys.argv[1]

with open("popular-names.txt") as f:
    data = f.readlines()
    start = len(data) - int(read)
    cnt = 0

    for i in range(len(data)):
        if start <= i:
            print(data[i].strip())

