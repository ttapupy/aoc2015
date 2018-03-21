#http://adventofcode.com/2015/day/14

#1

with open('Reindeer_Olympics.input', 'r') as f:
    reindeers=f.read()
    nochar=['can fly ', 'km/s for ', 'seconds, but then must rest for ', ]
    for i in nochar:
        if i in reindeers:
            reindeers=reindeers.replace(i, '')

    zoo={}        
    
    for sor in reindeers.splitlines():
        data = sor.split(' ')
        zoo.setdefault(data[0], [int(data[1]), int(data[2]), int(data[3])]) # rénszarvas: sebesség, haladás, pihenő
    print(zoo)


#Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, 
#what distance has the winning reindeer traveled?


distance=0
for k, v in zoo.items():
    base=int(2503 / (v[1] + v[2]))
    d=base  * v[0] * v[1]
    m = 2503 % (v[1] + v[2])
    if m > v[1]:
        p = v[1] * v[0]
    else:
        p = m * v[0]
    distance=max(distance, d+p)

print('A győztes által megtett út:', distance, '\n')

#2
with open('Reindeer_Olympics.input', 'r') as f:
    reindeers=f.read()
    nochar=['can fly ', 'km/s for ', 'seconds, but then must rest for ', ]
    for i in nochar:
        if i in reindeers:
            reindeers=reindeers.replace(i, '')

    zoo={}        
    points={}
    dist={}
    for sor in reindeers.splitlines():
        data = sor.split(' ')
        zoo.setdefault(data[0], [int(data[1]), int(data[2]), int(data[3])])  # rénszarvas: sebesség, haladás (mp), pihenő (mp)
        points.setdefault(data[0], 0)  # rénszarvas: pontok
        dist.setdefault(data[0], 0,)  # rénszarvas: megtett út
    print(zoo)


    
n=0

while n < 2503:
    for k, v in zoo.items():
        m = n % (v[1] + v[2])
        if m < v[1]:
            dist[k]=dist[k] + v[0]
    dd=max(dist.values())
    for l, w in dist.items():
        if w==dd:
            points[l]=points[l] + 1
    n+=1


print(points)
print(dist)
win=max(points, key=lambda x: points[x])
print('A győztes: ', win, ', aki ' , dist[win], ' km utat tett meg és ', points[win], ' pontot szerzett.', sep='')
