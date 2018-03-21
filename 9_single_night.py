#http://adventofcode.com/2015/day/9
#1
from itertools import permutations
with open('single_night.input', 'r') as f:
    betw={}
    cities=[]
    dist=[]
    city_list=[]
    d=0
    for sor in f.readlines():
        itin = sor.strip().split(" = ")
        dist=int(itin[1])
        d+=dist
        cities=itin[0].split(' to ')
        city_list.append(cities[0])
        city_list.append(cities[1])
        betw.update({tuple(cities): dist})
        betw.update({tuple(cities[::-1]): dist})
    sc=set(city_list)
    psc=(x for x in permutations(sc))
    for x in psc:
        a=0
        for i, y in enumerate(x[1::], 1):
            a = a + betw[(x[i-1], y)]
        if a < d:
            d = a
    print('A legrövidebb út:', d)
    
#2
with open('single_night.input', 'r') as f:
    betw={}
    cities=[]
    dist=[]
    city_list=[]
    d=0
    for sor in f.readlines():
        itin = sor.strip().split(" = ")
        dist=int(itin[1])
        cities=itin[0].split(' to ')
        city_list.append(cities[0])
        city_list.append(cities[1])
        betw.update({tuple(cities): dist})
        betw.update({tuple(cities[::-1]): dist})
    sc=set(city_list)
    psc=(x for x in permutations(sc))
    for x in psc:
        a=0
        for i, y in enumerate(x[1::], 1):
            a = a + betw[(x[i-1], y)]
        if a > d:
            d = a
    print('A leghosszabb út:', d)
