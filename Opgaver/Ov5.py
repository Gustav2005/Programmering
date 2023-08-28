print("Opgave 5")

V1=input("Indtast første variabel:")
V1=float(V1)
V2=input("Indtast anden variabel:")
V2=float(V2)
V3=input("Indtast tredje variabel:")
V3=float(V3)

Sum=V1+V2+V3

if Sum > 100:
    print("Summen af de tre variabler er over 100")
elif Sum == 100:
    print("Summen af de tre variabler er lig med 100")
else:
    print("Summen af de tre variabler er under 100")

print(f"Summen er {Sum}")
    
