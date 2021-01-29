#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

read = sys.argv[1]

with open("popular-names.txt") as f:
    data = f.readlines()
    for i in range(int(read)):
        print(data[i].strip())

