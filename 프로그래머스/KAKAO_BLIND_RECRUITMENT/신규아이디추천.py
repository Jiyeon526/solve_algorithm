def solution(new_id):
    answer = ''
    new_id += '.'
    newAnswer = new_id.lower()
    
    for s in newAnswer:
        if s.isalpha(): answer += s
        elif s.isdigit(): answer += s
        elif s == '-' or s == '_' or s == '.': 
            answer += s
            
    newAnswer = answer[0]
    for i in range(1, len(answer)):
        if answer[i-1] == '.' and answer[i] == '.': continue
        newAnswer += answer[i]
    
    if len(newAnswer) > 0 and newAnswer[-1] == '.':
        newAnswer = newAnswer[:-1]
        
    if len(newAnswer) > 0 and newAnswer[0] == '.':
        newAnswer = newAnswer[1:]
        
    if newAnswer == '':
        newAnswer += 'a'
    
    if len(newAnswer) >= 16:
        newAnswer = newAnswer[:15]
        if newAnswer[14] == '.':
            newAnswer = newAnswer[:14]
    
    if len(newAnswer) <= 2:
        while len(newAnswer) < 3:
            newAnswer += newAnswer[-1]

    answer = newAnswer
    return answer