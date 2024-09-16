def nQueens(N):
    board =[-1]*N
    rQueens(board,0,N)
    print(board)
    

def rQueens(board, current, size):
    if (current ==size):
        return True
    else:
        for i in range(size):
            board[current] = i
            if noConflicts(board, current):
                found = rQueens(board, current + 1, size)
                if found:
                    return True
    return False

def noConflicts(board, current):
    for i in range(current):
        if board[i]==board[current]:
            return False
        if current - i == abs(board[current] - board[i]):
            return False
    return True

nQueens(4)

board=[1,3,0,2]
..Q.
Q...
...Q
.Q..

[[.q..],
[...q],
[q...],
[..q.]]
n=len(board)
drawboard=["."]*n

drawboard=[['.']*4 for _ in range(4)]

for i in range(n):
    change=board[i]
    drawboard[change][i]="Q"
print(drawboard)













