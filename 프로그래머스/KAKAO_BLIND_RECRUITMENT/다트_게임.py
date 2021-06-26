def solution(dartResult):
    answer = [0]
    i = 0

    while i < len(dartResult):
        if (dartResult[i] + dartResult[i+1]).isdigit():
            score = int(dartResult[i] + dartResult[i+1])
            i = i+1
        else:
            score = int(dartResult[i])
        bonus = dartResult[i+1]

        if bonus == 'D':
            score = score ** 2
        elif bonus == 'T':
            score = score ** 3
        
        if i+2 < len(dartResult) and dartResult[i+2] == '*':
            answer[-1] = answer[-1] * 2
            score = score * 2
            i = i + 1 
        elif i+2 < len(dartResult) and dartResult[i+2] == '#':
            score = -score
            i = i + 1
        
        answer.append(score)
        i += 2

    return sum(answer)