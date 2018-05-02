# növeljünk egy karaktersort úgy, mintha szám lenne, aztán...
# http://adventofcode.com/2015/day/11

import re
password = 'cqjxjnds'

#1

no_char = re.compile(r"^((?![iol]).)*$")
two_pairs = re.compile(r".*([\w])\1.*([\w])\2.*")

def conse(lista):
    for i, e in enumerate(lista[2::],2):
        if ord(e)+1==(ord(lista[i-1])) and ord(e)+2==(ord(lista[i-2])):
            return True

pwl=[]
while pwl != len(password) * ['z']:
    pwl = list(password)[::-1]
    if conse(pwl) and re.search(no_char, password) and re.search(two_pairs, password):
        break
    else:
        for i in range(len(pwl)):
            if pwl[i] == 'z':
                pwl[i] = 'a'
                
            else:
                pwl[i] = chr(ord(pwl[i])+1)
                password = ''.join(pwl[::-1])
                break
print(password)



#2
