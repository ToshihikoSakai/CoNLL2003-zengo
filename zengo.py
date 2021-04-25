#coding: UTF-8
import os
import re
import glob
import pathlib
import pprint
import sys


args = sys.argv


filename = "./train.txt"

#key: 0... value:text
text = {}

#key:0... value:0 or 1
hit = {}


def Zengo(text,hit,k,n):
    start = k-n
    end = k+n+1
    hit[k] = 1

    if(start < 0):
        start = 0
    if(end > len(text)):
        end = len(text)
                
    for i in range(start,k):
        if(text[i] == []):
            continue
        if(text[i] == "\n"):
            start = i

    for i in range(k,end):
        if(text[i] == []):
            continue
        if(text[i] == "\n"):
            end = i
    
    for i in range(start,end):
        if(text[i] != "\n"):
            hit[i] = 1
            
    return hit


with open('{}'.format(filename),mode='r') as f:
    i = -1
    for s_line in f:
        i = i + 1
        if(s_line == "\n"):
            text[i] = "\n"
            continue
        s_line = s_line.rstrip()
        text[i] = s_line

f.close()
###################
###################
#textの中身は以下の通り
# i = 0, text[i] = -DOCSTART- -X- -X- O
# i = 1, text[i] = \n
# i = 2, text[i] = EU NNP B-NP B-ORG
# i = 3, text[i] =rejects VBZ B-VP O
###################
###################


for k,v in text.items():
    if(text[k] == "\n"):
        hit[k] = 1
        continue
        
    line = text[k].split()

    if(line[-1] != "O"):
        #前後n文字を残す
        hit = Zengo(text,hit,k,int(args[1]))


###################
###################
#hitの中身は以下の通り
# iは前後n文字にタグがないものは除外されているので、抜けれている番号がある
# i = 0, hit[i] = 1
# i = 1, hit[i] = 1
# i = 3, hit[i] = 1
###################
###################

for k,v in sorted(text.items()):
    if(k in hit):
        if(text[k]=="\n"):
            print(text[k],end='')
        else:
            print(text[k])

