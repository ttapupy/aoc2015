import os
os.system('cls' if os.name == 'nt' else 'clear')
#http://adventofcode.com/2015/day/5
#1
import re

vo=['a', 'e', 'i', 'o', 'u']
fo=['ab', 'cd', 'pq', 'xy']
s=0
reg1 = re.compile(r"(.)\1")
with open("nice_text.input", "r") as all:
    sorok=all.readlines()
    for sor in sorok:
        if [i for i in fo if i in sor]:
            continue
        if len([i for i in sor if i in vo]) > 2 and re.search(reg1, sor):
            s+=1
        else:
            continue
print(s)

#2


s=0

with open("nice_text.input", "r") as all:
    sorok=all.readlines()
    for sor in sorok:
        d = False
        #print('\n sor:', sor)
        for i, e in enumerate(sor[:-1:], 0):
            if e+sor[i+1] in sor[i+2::]:
                for j, f in enumerate(sor[:-2:], 0):
                    if f == sor[j+2]:
                        s+=1
                        break
            else:
                continue
            break
print(s)
'''
#2-nél talán vmi ilyesmi regex is működhet:
re.compile(r'(.)(.).*\1\2')
re.compile(r'(.).\1')
'''



                