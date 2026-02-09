# BFS 너비우선탐색
# 0: 길, 1: 벽
# 최단 경로 구하기 -> 한 개 까지 벽을 부수고 이동하기 가능
# 0이면 바로 이동 가능, 1이면 벽을 부쉈는지, 안부쉈는지 확인하고 이동

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
'''
[
    [0,1,0,0],
    [1,1,1,0],
    [1,0,0,0],
    [0,0,0,0],
    [0,1,1,1],
    [0,0,0,0]
]
'''
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)] # 각 좌표에 [0],[0]을 붙여놨음
'''
[
    [[1,0], [0,0], [0,0], [0,0]],
    [[0,0], [0,0], [0,0], [0,0]],
    [[0,0], [0,0], [0,0], [0,0]],
    [[0,0], [0,0], [0,0], [0,0]],
    [[0,0], [0,0], [0,0], [0,0]],
    [[0,0], [0,0], [0,0], [0,0]]
]
'''

def bfs():
    queue = deque([(0, 0, 0)]) # (x, y, 0:벽 안부순 상태 or 1:벽 부순 상태)
    visited[0][0][0] = 1 # 거리 1부터 시작

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y, broken = queue.popleft() # (0, 0, 0)
        if x == n - 1 and y == m -1:
            return matrix[x][y][broken]
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if matrix[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                        # 벽이 없으면서 과거에 아무도 이 칸에 도착한 적이 없다면
                        visited[nx][ny][broken] = visited[x][y][broken] + 1
                        # 이동했다고 생각하며 거리 +1추가
                        queue.append((nx, ny, broken))
                    elif matrix[nx][ny] == 1 and broken == 0:
