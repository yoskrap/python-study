n , m = map(int , input().split())

alist , blist = [],[]

for i in range(n):
    A = list(map(int , input().split()))
    alist.append(A)

for i in range(n):
    B = list(map(int , input().split()))
    blist.append(B)

for i in range(n):
    for j in range(m):
        result = alist[i][j] + blist [i][j]
        print(result , end = ' ')

    print()
