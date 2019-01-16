#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 21:59:52 2019

@author: aditiadeshshenoy
"""

fo = open("dataset_2_7.txt", "r")
line = fo.readlines()

seq = (line[0])
pat = (line[1])

n = (len(seq)-len(pat));
count = 0;

for i in range(n):
    if seq[i : (i+len(pat))] == pat[0:]:
        print (pat)
        print (seq[i : (i+len(pat)-1)]);
    
        count = (count + 1);


print (count)
    
        
        