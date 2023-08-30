print("Opgave 17")
from random import randint

Liste1=[]
Liste2=[]

for i in range(0, randint(10, 20)):
    Liste1.append(randint(100, 200))
    
for i in range(0,randint(10,20)):
    Liste2.append(randint(50,150))


if len(Liste1) > len(Liste2):
    print("Den første liste er længere end den anden liste")
elif len(Liste1) == len(Liste2):
    print("De to lister er lige lange")
else:
    print("Den anden liste er længere end den første liste")

print("Der er",len(Liste1),"elementer i den første liste")
print("Der er",len(Liste2),"elementer i den anden liste")

print(Liste1)
print(Liste2)