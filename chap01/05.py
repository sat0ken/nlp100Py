#!/usr/bin/env python3
# -*- coding: utf-8 -*-

str05    = "I am an NLPer".split(' ')
bi_gram1 = []
bi_gram2 = []

#単語bi_gramを作成
for i in range (len(str05)-1):
    tmp = []
    tmp.append(str05[i])
    tmp.append(str05[i+1])
    bi_gram1.append(tmp)

#文字bi_gramを作成
for i in str05:
    if len(i) != 1:
        for j in range (len(i)-1):
            bi_gram2.append(i[j] + i[j+1])

print(bi_gram1)
print(bi_gram2)
