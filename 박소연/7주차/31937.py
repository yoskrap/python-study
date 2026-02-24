import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
virusc = list(map(int, input().split()))
inp = []
graph = [[i] for i in range(n+1)]
for _ in range(m):
    inp.append(list(map(int, input().split())))
inp.sort()

for i in range(m):
    c1 = inp[i][1]; c2 = inp[i][2]
    graph[c2].extend(graph[c1])
    
for c in virusc:
    count = 0
    for where in virusc:
        if where == c:
            continue
        if c in graph[where]:
            count += 1
    if count == k-1:
        print(c)
        break