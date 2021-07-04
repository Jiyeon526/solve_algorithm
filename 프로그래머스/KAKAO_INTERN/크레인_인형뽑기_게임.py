def solution(board, moves):
    answer = 0
    crane = []
    
    for m in moves:
        doll, board = move(board, m)

        if len(crane) != 0  and crane[-1] == doll:
            crane.pop()
            answer += 2
        else:
            if doll != 0:
                crane.append(doll)
                
    return answer

def move(board, m):
    for j in range(len(board)):
        if board[j][m-1] == 0: continue
        else:
            tmp = board[j][m-1]
            board[j][m-1] = 0
            return tmp, board
    return 0, board