import os
os.system('cls' if os.name == 'nt' else 'clear') # törli a cmd-t az elején

import hashlib
a=0
#1
'''
while True:
    input = 'yzbqklnj'+ str(a)
    h5 = hashlib.md5(input.encode('utf-8')).hexdigest()[0:5]
    
    if h5 == '00000':
        print(a, h5)
        break
    
    a+=1
'''    
#2

while True:
    input = 'yzbqklnj'+ str(a)
    h6 = hashlib.md5(input.encode('utf-8')).hexdigest()[0:6]
    
    if h6 == '000000':
        print(a, h6)
        break
    
    a+=1
