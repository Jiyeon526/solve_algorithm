def solution(numbers, hand):
    answer = ''
    keypad = {1:['L', 0, 0], 2:[0, 1], 3:['R', 0, 2], 4:['L', 1, 0],
             5:[1, 1], 6:['R', 1, 2], 7:['L', 2, 0], 8:[2, 1], 9:['R', 2, 2],
             0:[3, 1], '*':['L', 3, 0], '#':['R', 3, 2]}
    
    Left = '*'
    Right = '#'
    for n in numbers:
        if str(keypad[n][0]).isalpha():
            answer += keypad[n][0]
            if answer[-1] == 'L': 
                Left = n
            else: 
                Right = n
        else:
            if len(keypad[Left]) == 3:
                L = abs(keypad[n][0] - keypad[Left][1]) + abs(keypad[n][1] - keypad[Left][2])
            else:
                L = abs(keypad[n][0] - keypad[Left][0]) + abs(keypad[n][1] - keypad[Left][1])
                
            if len(keypad[Right]) == 3:
                R = abs(keypad[n][0] - keypad[Right][1]) + abs(keypad[n][1] - keypad[Right][2])
            else:
                R = abs(keypad[n][0] - keypad[Right][0]) + abs(keypad[n][1] - keypad[Right][1])
            
            if L == R:
                if hand == 'right':
                    answer += 'R'
                    Right = n
                else:
                    answer += 'L'
                    Left = n
            elif L < R:
                answer += 'L'
                Left = n
            else:
                answer += 'R'
                Right = n
    return answer