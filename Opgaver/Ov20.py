print("Opgave 20")
      
n=int(input("Skriv startantallet af stjerner: "))

#n = 10

for k in range(n):
    s=""
    for j in range(n-k):
        s += "*"
    print(s)