print("Opgave 4")

Alder=input("Skriv din alder:")
Alder=float(Alder)

if 100 >= Alder >= 18:  
    print("Du er myndig :D")
elif  Alder > 100:
    print("Du er højst sandsynlig død")
elif Alder < 0:
    print("Du er ikke født")
else:
    print("Du er ikke myndig D:")