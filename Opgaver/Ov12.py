print("Opgave 12")
import math

a=float(input("Indtast a værdi: "))
b=float(input("Indtast b værdi: "))
c=float(input("Indtast c værdi: "))

d=(b**2)-(4*a*c)
print(d)

if d<0:
    print("Der er ingen løsninger")
elif d== 0:
    sol=-b/(2*a)
    print("Der er en løsning ",sol)
    print("Udregninger:",-b,"/",2*a,"=",sol)
else:
    sol1=(-b-math.sqrt(d))/(2*a)
    sol2=(-b+math.sqrt(d))/(2*a)
    print("Der er to løsninger",sol1,"og",sol2)
    print("Udregninger:",-b,"+/-",d**0.5,"/",2*a,"=",sol1,"og",sol2)

Topx=-b/(2*a)
Topy=-d/(4*a)


print(f"Toppunktet er ({Topx},{Topy})")


