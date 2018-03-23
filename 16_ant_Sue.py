# http://adventofcode.com/2015/day/16

tt={'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

with open('ant_Sue.input', 'r') as f:
    eml=f.read()
    ants={}
    dv=[]
    for sor in eml.splitlines():
        d=sor.split(':', 1)
        dv=d[1].split(',')
        for x in dv:
            y=x.strip().split(':')
            ants.setdefault(d[0], dict())[y[0]] = int(y[1])
    #print(ants)

    for k, v in ants.items():
        if v.items() <= tt.items():
            print('Sue néni száma:', k)
            break
