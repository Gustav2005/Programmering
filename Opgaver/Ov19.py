print("Opgave 19")


def udskrivtabel(x=0, b=1,y=10):
    print("")
    while x <= y:
        print(x)
        x=x+b


b = int(input("Skriv hvilken multiplikationstabel du vil have vist: "))
y = b*int(input("Skriv hvor mange gange tabellen skal gå op: "))

udskrivtabel(b=b, y = y)



