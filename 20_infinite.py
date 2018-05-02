#http://adventofcode.com/2015/day/20
# -*- coding: utf-8 -*-
from functools import reduce

def osztok(n):    
    return sum(set(reduce(lambda x, y: x+y ,((i , n//i) for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0))))


n=100000	# praktikusan egy a megoldásnál vélhetően kisebb számmal kezdem a while ciklust
while osztok(n)<3600000:
	n+=1
print(n)
