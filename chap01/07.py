#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sentense(x, y, z):
    return str(x) + '時の' + y +'は' +str(z)

if __name__ == '__main__':
    print(sentense(12, '温度', 22.4))
