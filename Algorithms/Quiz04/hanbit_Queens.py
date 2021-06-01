#1번

def EightQueens(a, n=8):
    board =[-1]*n
    count=0
    for i in range(n):
        board[0] = i
        for j in range(n):
            board[1]=j
            if not noConflicts(board, 1):
                continue
            for k in range(n):
                board[2] = k
                if not noConflicts(board, 2):
                    continue
                for l in range(n):
                    board[3] = l
                    if not noConflicts(board, 3):
                        continue
                    for m in range(n):
                        board[4] = m
                        if not noConflicts(board, 4):
                            continue
                        for o in range(n):
                            board[5] = o
                            if not noConflicts(board, 5):
                                continue
                            for p in range(n):
                                board[6] = p
                                if not noConflicts(board, 6):
                                    continue
                                for q in range(n):
                                    board[7] = q
                                    if noConflicts(board, 7):
                                        print (board)
                                        count+=1
                                        if count==a:
                                            return
    return

def noConflicts(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        if (current - i == abs(board[current] - board[i])):
            return False
    return True


#EightQueens(2)

#2번

def EightQueens2(board, n=8):
    nboard=[8]*8
    plusboard=[0]*8
    for ind, val in enumerate(board):
        if val != -1:
            nboard[ind]=1
            plusboard[ind]=val
    for i in range(nboard[0]):
        board[0] = i+plusboard[0]
        for j in range(nboard[1]):
            board[1]=j+plusboard[1]
            if not noConflicts(board, 1):
                continue
            for k in range(nboard[2]):
                board[2] = k+plusboard[2]
                if not noConflicts(board, 2):
                    continue
                for l in range(nboard[3]):
                    board[3] = l+plusboard[3]
                    if not noConflicts(board, 3):
                        continue
                    for m in range(nboard[4]):
                        board[4] = m+plusboard[4]
                        if not noConflicts(board, 4):
                            continue
                        for o in range(nboard[5]):
                            board[5] = o+plusboard[5]
                            if not noConflicts(board, 5):
                                continue
                            for p in range(nboard[6]):
                                board[6] = p+plusboard[6]
                                if not noConflicts(board, 6):
                                    continue
                                for q in range(nboard[7]):
                                    board[7] = q+plusboard[7]
                                    if noConflicts(board, 7):
                                        print (board)

    return

#EightQueens2([-1,4,-1,-1,-1,-1,-1,0])

#3번

def FourQueens(n=4):
    board = [[0,0,0,0],[0,0,0,0],
            [0,0,0,0],[0,0,0,0]]
    new_board=board
    for i in range(n):
        board[i][0] = 1
        for j in range(n):
            board[j][1] = 1
            if not noConflicts3(board, 1, j, n):
                board[j][1] = 0
                continue
            for k in range(n):
                board[k][2] = 1
                if not noConflicts3(board, 2, k, n):
                    board[k][2] = 0
                    continue
                for m in range(n):
                    board[m][3] = 1
                    if not noConflicts3(board, 3, m, n):
                        board[m][3] = 0
                        continue
                    print (board)
                    board[m][3] = 0
                board[k][2] = 0
            board[j][1] = 0
        board[i][0] = 0
    return

def noConflicts3 (board, current, qindex, n):
    for j in range(current):
        if board[qindex][j] == 1:
            return False
    k = 1
    while qindex - k >= 0 and current - k >= 0:
        if board[qindex - k][current - k] == 1:
            return False
        k += 1
    k = 1
    while qindex + k < n and current - k >= 0:
        if board[qindex + k][current - k] == 1:
            return False
        k += 1
    return True

#FourQueens()

###재귀함수 이용 Queens() = Queen의 수가 주어질 때 가능한 경우의 배열 출력

def Queens(n, place):
    board=[-1]*n
    for i in range(n):
        board[place]=i
        placequeen(n,board, place+1)

    return

def placequeen(n,board, place):
    if place == n-1:
        for i in range(n):
            board[place] = i
            if not noConflicts(board, place):
                continue
            print(board)
        return
    else:
        for i in range(n):
            board[place] = i
            if not noConflicts(board, place):
                continue
            placequeen(n,board, place+1)
    return

def noConflicts(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        if (current - i == abs(board[current] - board[i])):
            return False
    return True


if __name__=="__main__":

    n=int(input("Number of Queen:"))
    Queens(n,0)
