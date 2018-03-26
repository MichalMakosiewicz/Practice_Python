word = str(input("Wpisz słowo:"))

a = word[::-1]

print(a)

if a == word:
    print("Słowo jest polidromem")
else:
    print("Słowo nie jest polidromem")


