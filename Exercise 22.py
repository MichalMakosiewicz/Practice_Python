
imiona = {  }
with open('Imiona.txt', 'r') as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line in imiona:
            imiona[line] += 1
        else:
            imiona[line] = 1
        line = f.readline()

print(imiona)