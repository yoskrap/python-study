n = input()
ok = True

for i in range(len(n) // 2):
    if n[i] != n[-i - 1] : 
        ok = False 

if ok : 
    print(1)
else : 
    print(0)

