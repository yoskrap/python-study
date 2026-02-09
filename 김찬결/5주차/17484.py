import sys
input = sys.stdin.readline

n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]
'''
5 8 5 1
3 5 8 4
9 77 65 5
2 1 5 2
5 98 1 5
4 95 67 58
'''
for j in range(m): # 0열, 1열, 2열, 3열
    i = 0
    fuel = space[i][j]
    if i + 1 < n:
        down_dn = space[i + 1][j]
        if 0 <= j - 1 and j + 1 < m:
            left_dn = space[i + 1][j - 1]
            right_dn = space[i + 1][j + 1]
    
        elif j - 1 < 0 and j + 1 < m:
            right_dn = space[i + 1][j + 1]

        elif 0 <= j - 1 and j + 1 >= m:
            left_dn = space[i + 1][j - 1]
    
    fuel = max(fuel + le)