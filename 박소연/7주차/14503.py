n, m = map(int, input().split())
r, c, d = map(int, input().split())
wm = [list(map(int, input().split())) for _ in range(n)]
count = 0

while True:
    if wm[r][c] == 0:
        wm[r][c] = 2
        count += 1
        
    if wm[r-1][c] != 0 and wm[r][c-1] != 0 and wm[r+1][c] != 0 and wm[r][c+1] != 0:
        if d == 0:
            if r == n-1 or wm[r+1][c] == 1:
                break
            r += 1
            continue
        elif d == 1:
            if c == 0 or wm[r][c-1] == 1:
                break
            c -= 1
            continue
        elif d == 2:
            if r == 0 or wm[r-1][c] == 1:
                break
            r -= 1
            continue
        elif d == 3:
            if c == m-1 or wm[r][c+1] == 1:
                break
            c += 1
            continue
        
    if d != 0:
        d -= 1
    else:
        d = 3
        
    if d == 0:
        if wm[r-1][c] == 0:
            r -= 1
    elif d == 1:
        if wm[r][c+1] == 0:
            c += 1
    elif d == 2:
        if wm[r+1][c] == 0:
            r += 1
    elif d == 3:
        if wm[r][c-1] == 0:
            c -= 1
        
print(count)