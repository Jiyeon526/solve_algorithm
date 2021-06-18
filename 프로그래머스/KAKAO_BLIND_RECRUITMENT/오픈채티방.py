def solution(record):
    answer = []
    user = {}
    
    for r in record:
        word = list(map(str, r.split()))
        if word[0] == 'Leave': continue
        if word[1] not in user:
            user[word[1]] = word[2]
        else:
            user[word[1]] = word[2]
    
    for r in record:
        word = list(map(str, r.split()))
        if word[0] == 'Change': continue
        if word[0] == 'Enter':
            answer.append(user[word[1]] + "님이 들어왔습니다.")
        else:
            answer.append(user[word[1]] + "님이 나갔습니다.")

    return answer