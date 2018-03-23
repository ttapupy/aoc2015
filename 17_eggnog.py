cont=[11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3]
#http://adventofcode.com/2015/day/17
c=[11, 30, 11, 4]
import itertools as it
def eggnog(lst):
    kombi=0

    for i in range(3, len(lst)):
        for m in it.combinations(lst, i):
            if sum(m) == 150:
                kombi += 1
    return kombi


print(eggnog(cont))
#2
def eggnogmin(lst):
    minhossz=3
    minhosszdb=0
    for i in range(3, len(lst)):
        if i>minhossz and minhosszdb>0:
            break
        for m in it.combinations(lst, i):
            if sum(m) == 150:
                minhosszdb+=1
                minhossz=i
    return minhosszdb
print(eggnogmin(cont))