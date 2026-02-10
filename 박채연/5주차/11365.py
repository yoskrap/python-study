str = []
prt = []
cnt = 0

while (True) :
    str = input()
    if (str == "END") :
        break
    for i in range(len(str)-1, -1, -1) :
        prt.append(str[i])
    prt.append("\n")

for i in prt :
    print(i, end = '')