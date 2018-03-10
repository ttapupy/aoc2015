#http://adventofcode.com/2015/day/3
#1

with open("Houses.input", 'r') as all:
    route=all.read()
    NS={'^': 1, 'v': -1}
    WE={'<': -1, '>': 1}
    h=[[0,0]]
    x, y = 0, 0
    for i in route:
        if i in WE:
            x=x+WE[i]
        else:
            y=y+NS[i]
        h.append([x, y])
    s=set(map(tuple, h))
    l=len(s)
print(l)
    
#2
with open("Houses.input", 'r') as all:
    route=all.read()
    santa=(x for x in route[0::2])
    robo=(x for x in route[1::2])
    NS={'^': 1, 'v': -1}
    WE={'<': -1, '>': 1}
    h=[[0,0]]
    x, y = 0, 0
    for i in santa:
        if i in WE:
            x=x+WE[i]
        else:
            y=y+NS[i]
        h.append([x, y])
    x, y = 0, 0
    for i in robo:
        if i in WE:
            x=x+WE[i]
        else:
            y=y+NS[i]
        h.append([x, y])
    s=set(map(tuple, h))
    l=len(s)
print(l)

