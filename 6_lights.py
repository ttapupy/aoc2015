import os
os.system('cls' if os.name == 'nt' else 'clear')
#http://adventofcode.com/2015/day/6
'''
#1
with open("lights.input", "r") as allom:
    sorok=(sor.replace(',',' ').strip().split(' ') for sor in allom.readlines())
    on=set()
    off=set((x, y) for x in range(1000) for y in range(1000))
    toogle=set()
    for sor in sorok:
        
        if sor[0]=='turn_on':
            on.update(z for z in ((x, y) for x in range(int(sor[1]), int(sor[4])+1) for y in range(int(sor[2]), int(sor[5])+1)))
            off=off-on
        elif sor[0]=='turn_off':
            off.update(z for z in ((x, y) for x in range(int(sor[1]), int(sor[4])+1) for y in range(int(sor[2]), int(sor[5])+1)))
            on=on-off
        else:
            toogle=set(z for z in ((x, y) for x in range(int(sor[1]), int(sor[4])+1) for y in range(int(sor[2]), int(sor[5])+1)))
            t_on=(toogle-on)
            on=(on-toogle)
            on.update(t_on)
            t_off=(toogle-off)
            off=(off-toogle)
            off.update(t_off)

                
    print(len(on))
'''
#2

with open("lights.input", "r") as allom:
    sorok=(sor.replace(',',' ').strip().split(' ') for sor in allom.readlines())
    on=set()
    toogle=set()
    off=((x, y) for x in range(1000) for y in range(1000))
    bright={x:0 for x in off}
        
    for sor in sorok:
        
        if sor[0]=='turn_on':
            on=((x, y) for x in range(int(sor[1]), int(sor[4])+1) for y in range(int(sor[2]), int(sor[5])+1))
            for t in on:
                    bright[t]+=1
                    #print(bright[t])
            #off=off-on
        elif sor[0]=='turn_off':
            off = ((x, y) for x in range(int(sor[1]), int(sor[4])+1) for y in range(int(sor[2]), int(sor[5])+1))
            for t in off:
                if bright[t] > 0:
                        bright[t]-=1
            #on=on-off
        else:
            toogle=((x, y) for x in range(int(sor[1]), int(sor[4])+1) for y in range(int(sor[2]), int(sor[5])+1))
            for t in toogle:
                    bright[t]+=2

                
    print(sum(bright.values()))