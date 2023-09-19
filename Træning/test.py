'''
karakterer = [10,10,12,10,10,7,10,12,12,0]

s=0

for k in karakterer:
    s+=k

    print (s)
'''

tekst = "Hej med dig menneske"

d={}

for b in tekst:
    if b not in d:
        d[b] = 1
    else:
        d[b] += 1
    
print(d)
   
    