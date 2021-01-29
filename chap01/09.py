#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

str09 = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
str09 = str09.replace(":", "").replace(".", "")
arr = str09.split()

for word in arr:
    if len(word) <= 4:
        print(word)
    else:
        first = word[0]
        last = word[len(word)-1]
        middle = word[0:len(word)-2]
        first += ''.join(random.sample(middle, len(middle)))
        first += last
        print(first)
