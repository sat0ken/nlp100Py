#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

str03 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str03 = str03.replace('.', '')
arr   = []

for i in (str03.split(' ')):
    arr.append(len(i))

print(arr)
