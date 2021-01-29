#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("popular-names.txt") as f:
    lines = f.readlines()
    for line in lines:
        print(line.replace("\t", " ").strip())
