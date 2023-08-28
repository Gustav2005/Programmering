print("Opgave 9")

tal=1
liste=0

while tal <= 100:
    if tal%2==0:
        print(tal)
        liste+=tal
    tal+=1

print(liste)