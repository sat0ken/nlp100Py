#!/usr/bin/env python3
# -*- coding: utf-8 -*-

str04     = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str04_arr = str04.replace('.', '').split(' ')
num_arr   = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dict      = {}

for i in range (len(str04_arr)):
    if i+1 in num_arr:
        dict[str04_arr[i][0:1]] = i+1
    else:
        dict[str04_arr[i][0:2]] = i+1

for key, value in (sorted(dict.items(), key=lambda x: x[1])):
    print(key, value)
