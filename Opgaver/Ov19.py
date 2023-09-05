print("Opgave 19")


def udskrivtabelxb(x=0, b=1,y=10):
    print("")
    while x <= y:
        print(x)
        x=x+b


b = int(input("Skriv hvilken multiplikationstabel du vil have vist:"))
y = int(input("Skriv hvilken slutværdi tabellen skal have:"))

udskrivtabelxb(b=b, y = y)



