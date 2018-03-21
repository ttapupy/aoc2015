
#http://adventofcode.com/2015/day/13
from itertools import permutations
#1
with open('dinner_table.input', 'r') as f:
    happiness=f.read()
    happiness=happiness.replace('lose ', '-')
    happiness=happiness.replace('would ', '')
    happiness=happiness.replace('gain ', '')
    happiness=happiness.replace('.', '')
    happiness=happiness.replace(' happiness units by sitting next to', '')
    pers=set()
    rel={}
    for sor in happiness.splitlines():
        hap=sor.split(' ')
        pers.add(hap[0])
        rel.setdefault(hap[0], dict())[hap[2]] = int(hap[1])
    print(rel)
    print(pers)
o=0

for z in permutations(pers):
    w=list(z)
    w.append(w.pop(0))
    h = sum(map(lambda x, y: rel[x][y], z, w)) + sum(map(lambda x, y: rel[x][y], w, z))
    o = max(o, h)
print(o)
#2
with open('dinner_table.input', 'r') as f:
    happiness=f.read()
    happiness=happiness.replace('lose ', '-')
    happiness=happiness.replace('would ', '')
    happiness=happiness.replace('gain ', '')
    happiness=happiness.replace('.', '')
    happiness=happiness.replace(' happiness units by sitting next to', '')
    pers=set()
    rel={}
    for sor in happiness.splitlines():
        hap=sor.split(' ')
        pers.add(hap[0])
        rel.setdefault(hap[0], dict())[hap[2]] = int(hap[1])
        rel.setdefault('Me', dict())[hap[2]] = 0
        rel.setdefault(hap[0], dict())['Me'] = 0
    pers.add('Me')
    print(rel)
    print(pers)

o=0

for z in permutations(pers):
    w=list(z)
    w.append(w.pop(0))
    h = sum(map(lambda x, y: rel[x][y], z, w)) + sum(map(lambda x, y: rel[x][y], w, z))
    o = max(o, h)
print(o)