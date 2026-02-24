h, n = map(int, input().split())
wh = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    r, c = map(int, input().split())
    wh.append((r, c, i))
wh.sort()

res = [0] * n
for i in range(n):
    whidx = wh[2]
    res[whidx] = i+1
    
print("YES")
for i in range(n):
    print(res[i], end=' ')