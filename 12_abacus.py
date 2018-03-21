#http://adventofcode.com/2015/day/12

import json

#1
with open("abacus.json", 'r') as f:
    adat=f.read()
    jel=[':', '[', ']', '{', '}']
    for i in jel:
        if i in adat:
            adat=adat.replace(i, ',')
   
    data=adat.split(',')
    print(type(data))
    nrs=0
    for x in data:
        try:
            if str(int(x) * 1) == x:
                nrs+=int(x)
        except ValueError: 
            pass
    print(nrs)

#2

def summa(obj):
    if type(obj) is int:
        return obj
    if type(obj) is list:
        return sum(map(summa, obj))
    if type(obj) is dict:
        ertek = obj.values()
        if "red" in ertek:
            return 0
        return sum(map(summa, ertek))
    else:
        return 0

with open("abacus.json", 'r') as f:
    adat2=f.read()
    obj = json.loads(adat2)
    print(summa(obj))