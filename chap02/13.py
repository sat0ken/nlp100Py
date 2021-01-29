#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def colread(path):
    with open(path, mode='r') as f:
        data = f.readlines()
        return data

def merge(path, data1, data2):
    with open(path, mode='w') as f:
        for i in range(len(data1)):
            f.write(data1[i].strip()+"\t"+data2[i])

col1 = colread("col1.txt")
col2 = colread("col2.txt")
merge("merged.txt", col1, col2)
