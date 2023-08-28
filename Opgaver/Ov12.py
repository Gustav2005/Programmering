print("Opgave 12")
import math

a=float(input("Indtast a værdi: "))
b=float(input("Indtast b værdi: "))
c=float(input("Indtast c værdi: "))

d=(b**2)-(4*a*c)
print(d)

sol1=(-b-math.sqrt(d))/(2*a)
sol2=(-b+math.sqrt(d))/(2*a)

Topx=-b/(2*a)
Topy=-d/(4*a)


print(f"Nulpunkterne for formlen er {sol1} og {sol2}")
print(f"Toppunktet er ({Topx},{Topy})")


