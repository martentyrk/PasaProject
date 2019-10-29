file = "Isikukoodid.csv"

with open(file, 'r', encoding="UTF-8") as f:
    l = f.read().splitlines()
    for i in range(len(l)):
        l[i] = l[i].split(',')


line1 = "Eesnimi: "
line2 = "Perenimi: "
line3 = "Isikukood: "

for isik in l:
    line1 = "Eeesnimi: {0}".format(isik[0])
    line2 = "Perenimi: {0}".format(isik[1])
    line3 = "Isikukood: {0}".format(isik[2])
    print(line1 + '\n' + line2 + '\n' + line3 + '\n' + len(line3) * '-')