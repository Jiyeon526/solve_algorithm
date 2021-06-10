def solution(rows, columns, queries):
    answer = []
    board = [[] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(columns):
            board[i].append((i) * columns + j + 1)
    
    for x1, y1, x2, y2 in queries:
        x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
        tmp = board[x1][y1]
        arr_min = tmp
        
        for i in range(x2-x1):
            arr_min = min(arr_min, board[x1+1+i][y1])
            board[x1+i][y1] = board[x1+1+i][y1]
            
        for i in range(y2-y1):
            arr_min = min(arr_min, board[x2][y1+1+i])
            board[x2][y1+i] = board[x2][y1+1+i]
        
        for i in range(x2-x1):
            arr_min = min(arr_min, board[x2-1-i][y2])
            board[x2-i][y2] = board[x2-1-i][y2]
        
        for i in range(y2-y1):
            arr_min = min(arr_min, board[x1][y2-1-i])
            board[x1][y2-i] = board[x1][y2-1-i]
            
        board[x1][y1+1] = tmp
        answer.append(arr_min)
        
    return answer