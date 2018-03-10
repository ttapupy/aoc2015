# http://adventofcode.com/2015/day/2

#1

with open("No_Math.input", 'r') as all:
    sorok=([int(i) for i in sor.split('x')] for sor in all.readlines(7))
    print(sorok)
    feet=0
    l, w, h = 0, 0, 0
    for sor in sorok:
        l, w, h = sor[0], sor[1], sor[2]
        feet = 2*l*w + 2*w*h + 2*h*l + sorted(sor)[0]*sorted(sor)[1] + feet
print(feet)

#2

with open("No_Math.input", 'r') as all:
    sorok=([int(i) for i in sor.split('x')] for sor in all.readlines())
    feet=0
    l, w, h = 0, 0, 0
    for sor in sorok:
        l, w, h = sor[0], sor[1], sor[2]
        feet = l*w*h + 2*(sorted(sor)[0]+sorted(sor)[1]) + feet
print(feet)