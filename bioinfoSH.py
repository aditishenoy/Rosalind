#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 21:50:38 2019

@author: aditiadeshshenoy
"""

file = open("dataset_2_10.txt", "r")
line = file.readlines()

seq = (line[0])
#k = (line[1])
#k = k.rstrip()
def CountDNA(seq):
    n = len(seq)
    c1=c2=c3=c4 = 0
    for i in range(n):
        if seq[i] =='A':
            c1 += 1
        elif seq[i] == 'C':
            c2 += 1
        elif  seq[i] == 'G':
            c3 += 1
        else:
            c4 += 1
    return (c1, c2, c3, c4)

if __name__ == '__CountDNA__':
    CountDNA()
    

def Transcribe(seq):
    n = len(seq)
    rna = []
    for i in range (n):
        if seq[i] =='T':
            rna += "U"
        else:
            rna += seq[i]
    str1 = ''.join(rna)
    return (str1)

if __name__ == '__Transcribe__':
    Transcribe()
        
def Complement(seq):
    n = len(seq)
    com = []
    comr = []
    for i in range(n):
        if seq[i] =='A':
            com += "T"
        elif seq[i] == 'C':
            com += "G"
        elif  seq[i] == 'G':
            com += "C"
        else:
            com += "A"
    comr = com[::-1]
    str1 = ''.join(comr)
    return (str1)
    
if __name__ == '__Complement__':
    Complement()
    
def Fibo(n,k):
    i = 0
    cm = 0
    cn = 1
    sum = 1
    while (i<=n):
        if (i%2 == 0):
            cn = k

        else: 
            cm = cn
            sum += (cm + cn)
        i +=1
    
    return (sum)

    
if __name__ == '__Fibo__':
    Fibo()    
    
    
#def GCContent()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    