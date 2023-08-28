print("Opgave 13")

#Retvinklet trekant
t=input("Er trekanten retvinklet (j/n): ")
if t=="j":
    t==input("Kender vi hypotenuse og katete (j/n): ")
    if t=="j":
        a=float(input("Indtast katete:"))
        b=float(input("Indtast hypotenuse:"))
        print ("Den anden katete er:",(b**2-a**2)**0.5 )
    else:
        a=float(input("Indtast katete: "))
        b=float(input("Indtast katete: "))
        print("Hypotenusen er:",(a**2+b**2)**0.5 )