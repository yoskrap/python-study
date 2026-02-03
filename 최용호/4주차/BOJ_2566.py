board = [[0] * 10]

for i in range(9):
    A = list(map(int , input().split()))
    A.insert(0,0)
    board.append(A)

max = board[0][0]
ans = [1 , 1]
for i in range(10):
    for j in range(10):
        if board[i][j] > max:
            max = board[i][j]
            ans[0] = i 
            ans[1] = j

print(max)
print(ans[0] , ans[1])