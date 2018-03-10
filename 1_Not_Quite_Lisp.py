# http://adventofcode.com/2015/day/1

#1
with open("Not_Quite_Lisp.input", 'r') as all:
    text=all.read()
    f=0
    for i, e in enumerate(text):
        if e=='(':
            f+=1
        else:
            f-=1
print (f, i+1)

#2
with open("Not_Quite_Lisp.input", 'r') as all:
    text=all.read()
    f=0
    for i, e in enumerate(text):
        if e=='(':
            f+=1
        else:
            f-=1
        if f==-1:   
            break   
print (f, i+1)