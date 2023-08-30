print("Opgave 18")
from random import randint

Liste1=[]
Liste2=[]

for i in range(0,2):
    Liste1.append(randint(1,2))
    Liste2.append(randint(1,2))

print(Liste1)
print(Liste2)

if Liste1 == Liste2:
    print("De to lister er lig med hinanden")
else:
    print("De to lister er ikke lig med hinanden")
    
