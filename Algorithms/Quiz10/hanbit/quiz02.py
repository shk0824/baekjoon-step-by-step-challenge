def nQueens(board):
    N=len(board)
    placed=[]
    for i in range(N):
        if board[i]!=-1:
            placed.append(i)
    rQueens(board,0,N,placed)
    if -1 in board:
        print("not possible")
        return
    xboard=[["."]*N for _ in range(N)] # "."으로 된 새로운 보드 생성
    print(board)
    for ind,val in enumerate(board): # 퀸 위치의 "."을 Q로 바꾸기
        xboard[val][ind]='Q'
    for row in xboard: #각 행마다 띄우면서 원소는 한 칸 공백 두고 출력
        for col in row:
            print(col, end=" ") 
        print()

def rQueens(board, current, size,placed):
    if current in placed:
        if rQueens(board, current+1, size, placed):
            return True
        else:
            return False
    
    if (current ==size):
        return True
    else:
        for i in range(size):
            board[current] = i
            if noConflicts(board, current,size):
                found = rQueens(board, current + 1, size,placed)
                if found:
                    return True
    return False

def noConflicts(board, current,size):
    for i in range(size):
        if i == current:
            continue
        if board[i]==board[current]:
            return False
        if current - i == abs(board[current] - board[i]):
            return False
    return True

Location=[-1,-1,4,-1,-1,-1,-1,0,-1,5]
nQueens(Location)



