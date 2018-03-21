#Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
#Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
#Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
#Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8
sugar=[3, 0, 0, -3, 2]
sprinkles=[-3, 3, 0, 0, 9]
candy=[-1, 0, 4, 0, 1]
choko=[0, 0, -2, 2, 8]
ingr=[sugar,sprinkles,candy,choko]
prop=[list(i) for i in zip(*ingr)] #capacity, durability, flavor, texture, calories
cal=prop[4]
import itertools as it
#1
'''
spoons= it.product([a for a in range(1,98)], repeat=4)
max_score=0
for spoon in spoons:
    if sum(spoon)==100:
        prop_score = 1
        for pr in range(4):
            prop_value = 0
            for ir in range(4):
                prop_value+=(spoon[ir]*prop[pr][ir])
            if prop_value<0:
                prop_value=0
            prop_score*=prop_value
        max_score=max(max_score, prop_score)
print(max_score) # 222870
'''
#2
spoons= it.product([a for a in range(1,98)], repeat=4)
max_score=0
for spoon in spoons:
    if sum(spoon)==100:
        prop_score = 1
        for pr in range(4):
            prop_value = 0
            calories = 0
            for ix, c in enumerate(cal):
                calories+=spoon[ix]*c
                if calories==500:
                    for ir in range(4):
                        prop_value+=(spoon[ir]*prop[pr][ir])
                    if prop_value<0:
                        prop_value=0
                    prop_score*=prop_value
        max_score=max(max_score, prop_score)
print(max_score) # 117936




