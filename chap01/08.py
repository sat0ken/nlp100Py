#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def cipher(word):
    for i in word:
        if i.islower():
            print(219 - ord(i))
        else:
            print(i)

if __name__ == '__main__':
    cipher('hoge')
