#!/usr/bin/env python3
# -*- coding: utf-8 -*-

str1 = "パトカー"
str2 = "タクシー"
str3 = ""

for i, j in zip(str1, str2):
    str3 += i.lstrip() + j.lstrip()

print(str3)
