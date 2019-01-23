#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 21:59:52 2019

@author: aditiadeshshenoy
"""
#Code Challenge 1: Implemented PatternCount (1.2)
fo = open("dataset_2_10.txt", "r")
line = fo.readlines()

seq = (line[0])
k = (line[1])
k = k.rstrip()

def PatternCount(Text,Pat):
    n = (len(seq)-len(Pat));
    count1 = 0;
    for i in range(n):
        if seq[i : (i+len(Pat))] == Pat[0:]:
        #print (pat)
        #print (seq[i : (i+len(pat)-1)]);
            count1 = (count1 + 1);
    return (count1)


if __name__ == '__PatternCount__':
    PatternCount()
    
 
#Code Challenge 2: Solve the Frequent Words Problem (1.2)
def FrequentWords(Text, k):
    fp = []
    fp1 = []
    n = (len(seq)- int(k));
    count = {}

    for i in range(n):
        patt = seq[i:(i+int(k))]
        #print (patt)
        #print (PatternCount(seq,patt))
        count [i] = (PatternCount(seq,patt))
    #print (count)
    mcount = max(count.values());
    #print (mcount)
    
    for i in range(n):
        if count[i] == mcount:
            fp.append(seq[i:(i+int(k))])
            fp1 = list(dict.fromkeys(fp))
    return (fp1)
     
if __name__ == '__FrequentWords__':
    FrequentWords()
    
    
f1= open("dataset_3_2.txt", "r")
lines = f1.readlines()  
seq1 = (lines[0])
    
#seq1 = 'AAAACCCGGT'
#Code Challenge 3: Solve the Reverse Complement Problem (1.3)  
def ReverseComplement(seq1):
    l = len(seq1)
    seq2 = ''
    for i in range(l):
        if seq1[i] == 'A':
            seq2 += 'T'
        elif seq1[i] == 'T':
            seq2 += 'A'
        elif seq1[i] == 'G':
            seq2 += 'C'
        else:
           seq2 += 'G'
          
    return (seq2[::-1]
)


if __name__ == '__ReverseComplement__':
    ReverseComplement()



