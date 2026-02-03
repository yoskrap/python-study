from collections import deque

n, m, v = map(int, input().split())

# graph 만들기 
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# dfs 구현하기 (recursion)
def dfs_r(cur):
    visited[cur] = 1
    print(cur, end=' ')
    for nxt in range(1, n+1):
        if graph[cur][nxt] == 1 and not visited[nxt]:
            dfs_r(nxt)

def dfs_stack(start):
    visited = [0]*(n+1)
    stack = [start]
    ans = []
    while stack:
        cur = stack.pop()
        if visited[cur]:
            continue
        visited[cur] = 1
        ans.append(cur)
        # 작은 번호부터 방문하려면 큰 번호부터 push
        for nxt in range(n, 0, -1):
            if graph[cur][nxt] == 1 and not visited[nxt]:
                stack.append(nxt)
    print(*ans)

def bfs(start):
    visited = [0]*(n+1)
    q = deque([start])
    visited[start] = 1
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for nxt in range(1, n+1):
            if graph[cur][nxt] == 1 and not visited[nxt]:
                visited[nxt] = 1
                q.append(nxt)

visited = [0]*(n+1)


dfs_r(v)
print()
dfs_stack(v)
bfs(v)
