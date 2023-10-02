print("Opgave 22")

i = 0
f = open("Test.txt", "r")
for line in f:
    if i % 2 == 0:
        print(line)
    i += 1
