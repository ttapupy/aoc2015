import os
os.system('cls' if os.name == 'nt' else 'clear')
#http://adventofcode.com/2015/day/8
#1

with open('Matchsticks.input', 'r') as all:
    sorok=all.read().splitlines()
    qq=2* len(sorok)

    n=0
    ns=[]
    
    for sor in sorok:
        while '\\\\' in sor:
            sor=sor.replace('\\\\','', 1)
            n+=1
        while '\\x' in sor:
            sor = sor.replace('\\x','', 1)
            n+=3
        while '\\"' in sor:
            sor = sor.replace('\\"','', 1)
            n+=1
        ns.append(sor)        
    print(n+qq)
    #print(ns)
    

with open('Matchsticks.input', 'r') as all:
    sorok=all.read().splitlines()
    qq=2* len(sorok)

    n=0
    ns=[]
    
    for sor in sorok:
        while '\\\"' in sor:
            sor=sor.replace('\\\"','', 1)
            n+=2
        while '\"' in sor:
            sor = sor.replace('\"','', 1)
            n+=1
        while '\\' in sor:
            sor = sor.replace('\\','', 1)
            n+=1
        ns.append(sor)        
    print("2.:", n+qq)
    print(ns)