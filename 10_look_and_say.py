import os
os.system('cls' if os.name == 'nt' else 'clear')
# http://adventofcode.com/2015/day/10
import re
#1
k='1321131112'
s=[]
rx=re.compile(r'((.)\2*)')
n=0
while n < 40:
    b=[x for x in re.findall(rx, k)]
    sn=[]
    for x in b:
        sn.append(str(len(x[0]))+x[1])
    s.append(''.join(sn))
    k=s[-1]
    n+=1
print(k)
print('A 40. elem hossza:', len(k)) #492982
'''
#2 maradtam a brute force -nál, végülis ez uaz, mint az 1., picit optimalizálva
k='1321131112'
rx=re.compile(r'((.)\2*)')
n=0
l=0
while n < 50:
    b=(x for x in re.findall(rx, k))
    sn = [str(len(x[0]))+x[1] for x in b]
    l=len(sn)
    k=''.join(sn)
    n+=1
print('Az 50. elem hossza:', len(k)) # 6989950
'''





