#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 21:59:52 2019

@author: aditiadeshshenoy
"""
#Code Challenge 1: Implemented PatternCount (1.2)
fo = open("dataset_2_7.txt", "r")
line = fo.readlines()

seq = (line[0])
pat = (line[1])
pat = pat.rstrip()

def PatternCount(Text,Pat):
    n = (len(seq)-len(pat));
    count = 0;
    for i in range(n):
        if seq[i : (i+len(pat))] == pat[0:]:
        #print (pat)
        #print (seq[i : (i+len(pat)-1)]);
            count = (count + 1);
    return (count)


if __name__ == '__PatternCount__':
    PatternCount()
    
 
#Code Challenge 2: Solve the Frequent Words Problem (1.2)
def FrequentWords(Text, k):
    fp = []
    n = (len(seq)- k );
    count = []
    for i in range(n):
        patt = seq[i:k]
        #print (count[i])
        count.append(PatternCount(seq,patt))
    mcount = max(count);
    
    for i in range(n):
        if count[i] == mcount:
            fp = seq[i:k] 
            fp1 = list(dict.fromkeys(fp))
    return fp1
     
if __name__ == '__FrequentWords__':
    FrequentWords()