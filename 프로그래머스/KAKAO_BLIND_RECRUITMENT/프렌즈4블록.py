def solution(m, n, board):
    answer = 0
    
    while True:
        visit = [[False for _ in range(n)] for _ in range(m)]
        nowCnt = clear(board, visit, m, n)
        if nowCnt == 0: break
        answer += nowCnt
        
        print("nowCnt = ", nowCnt)
        for i in range(m):
            print(*board[i])
        print()
        for i in range(m):
            print(*visit[i])
        print()
        board = newMap(board, visit, m, n)
        for i in range(m):
            print(*board[i])
        print("=======================================================")
    
    return answer

def clear(board, visit, m, n):
    cnt = 0
    
    for i in range(m):
        for j in range(n):
            nowBlock = board[i][j]
            if i+1 >= m or j+1 >=n: continue
            if nowBlock != '0' and nowBlock == board[i+1][j] and nowBlock == board[i][j+1] and nowBlock == board[i+1][j+1]:
                if visit[i][j] == False:
                    cnt += 1
                if visit[i][j+1] == False:
                    cnt += 1
                if visit[i+1][j] == False:
                    cnt += 1
                if visit[i+1][j+1] == False:
                    cnt += 1
                visit[i][j] = visit[i+1][j] = visit[i][j+1] = visit[i+1][j+1] = True
                
    return cnt

def newMap(board, visit, m, n):
    newBoard = [['0' for _ in range(n)] for _ in range(m)]
    
    for j in range(n):
        k = m-1
        for i in range(m-1, -1, -1):
            if visit[i][j]: continue
            newBoard[k][j] = board[i][j]
            k -= 1
    
    return newBoard

m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m, n, board))