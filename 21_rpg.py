'''
http://adventofcode.com/2015/day/21
Pontjaim: 100
    damage: ?
    armor: ?
Boss :
    Hit Points: 104
    Damage: 8
    Armor: 1

Meglátásom szerint egyformának vagy nagyobbnak kell lennie az én támadóerőm (y) és a Boss páncélja közti különbségnek, mint az ő támadóereje és az az én páncélom (x) különbsége.
Tehát 8-x <= y-1
8-x <= y-1
9 <= x + y <= 10 elégséges <-- Ezen variációk közül a legkisebb költségűt keressük.

A 2. részben is szűkítek: 8 <= x + y <= 9
''' 

from itertools import product as szorz

weapon = {4:'Dagger', 5:'Shortsword', 6:'Warhammer', 7:'Longsword', 8:'Greataxe' }
armor = {0:'no_armor', 1:'Leather', 2:'Chainmail', 3:'Splintmail', 4:'Bandedmail', 5:'Platemail'}
ring_dam = {0:'no_rdam', 1:'Damage_1', 2:'Damage_2', 3:'Damage_3'}
ring_def = {0:'no_rdef', 1:'Defense_1', 2:'Defense_2', 3:'Defense_3'}

cost = {'Dagger':8, 'Shortsword':10, 'Warhammer':25, 'Longsword':40, 'Greataxe':74, 'Leather':13, 'Chainmail':31, 'Splintmail':53, 'Bandedmail':75, 'Platemail':102, 'Damage_1':25, 'Damage_2':50, 'Damage_3':100, 'Defense_1':20, 'Defense_2':40, 'Defense_3':80, 'no_rdam':0, 'no_rdef':0, 'no_armor':0}
weapon_list=list(weapon.keys())
armor_list=list(armor.keys())
ring_dam_list=list(ring_dam.keys())
ring_def_list=list(ring_def.keys())
cost_list=list(cost.values())

pwr=[weapon, armor, ring_dam, ring_def]
ok=[]
not_ok=[]

def csata(pp, pw, pa, ep, ew, ea):
    while True:
        ep -= max(pw - ea, 1)
        if ep <= 0:
            return True
        pp -= max(ew - pa, 1) 
        if pp <= 0:
            return False

for i in szorz(weapon_list, armor_list, ring_dam_list, ring_def_list):
    if 9 <= sum(i) <=10:
        ok.append(i)


for i in szorz(weapon_list, armor_list, ring_dam_list, ring_def_list):  # a 2. részhez
    if 8 <= sum(i) <=9:
        not_ok.append(i)

pwr_ok=[]
pwr_not_ok=[]

enemy = [104, 8, 1]

for j in ok:
    player=[100, j[0]+j[2], j[1]+j[3]]
    if csata(*player, *enemy):
        t=[]
        for r in range(4):
            t.append(pwr[r][j[r]])
        pwr_ok.append(t)

mini=999
mini_list=[]
for x in pwr_ok:
    c=0
    for y in x:
        c=c+cost[y]
    if c<mini:
        mini=c
        mini_list=x
print(mini)
print(mini_list)

# a 2. részhez:
for j in not_ok:
    player=[100, j[0]+j[2], j[1]+j[3]]
    if not csata(*player, *enemy):
        t=[]
        for r in range(4):
            t.append(pwr[r][j[r]])
        pwr_not_ok.append(t)


maxi=0
maxi_list=[]
for x in pwr_not_ok:
    c=0
    for y in x:
        c=c+cost[y]
    if c>maxi:
        maxi=c
        maxi_list=x
print(maxi)
print(maxi_list)




