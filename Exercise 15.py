
def make_list():
    x = input("Wpisz zdanie:")
    y = x.split()
    return y

def reverse():
    x = list(reversed(make_list()))
    return x

print(reverse())


