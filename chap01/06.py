#!/usr/bin/env python3
# -*- coding: utf-8 -*-

str1    = "paraparaparadise"
str2    = "paragraph"
wa_list = []

def bi_gram(str_bi_gram):
    rtnarr = []
    for i in range (len(str_bi_gram)-1):
        char2 = str_bi_gram[i] + str_bi_gram[i+1]
        if char2 not in rtnarr:
            rtnarr.append(char2)

    return rtnarr

def check_set(style, arr1, arr2):
    rtnarr = []
    for i in arr1:
        if style == 'sa' and i not in arr2:
            rtnarr.append(i)
        elif style == 'seki' and i in arr2:
            rtnarr.append(i)

    return rtnarr

if __name__ == '__main__':
    str1_arr = bi_gram(str1)
    str2_arr = bi_gram(str2)

    #和集合
    wa_list = str1_arr + str2_arr
    print('和集合   ：  ', sorted(set(wa_list), key = wa_list.index))

    #積集合
    print('積集合   ：  ', check_set('seki', str1_arr, str2_arr))

    #差集合
    print('差集合(X-Y)：', check_set('sa', str1_arr, str2_arr))
    print('差集合(Y-X)：', check_set('sa', str2_arr, str1_arr))

    if 'se' in str1_arr:
        print('seはXに含まれる')
    elif 'se' in str2_arr and 'se' not in str1_arr:
        print('seはYに含まれる')
    else:
        print('seはどちらにも含まれない')
