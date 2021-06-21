def solution(n, arr1, arr2): 
    answer = []
    
    for i in range(n):
        tmp = arr1[i] | arr2[i]
        tmpWord = bitOper(tmp)
        if len(tmpWord) != n:
            ansWord = " " * (n-len(tmpWord)) + tmpWord
            answer.append(ansWord)
        else:
            answer.append(tmpWord)
   
    print(answer)
    return answer

def bitOper(N):
    word = ""
    
    if N < 2:
        if N == 1: return "#"
        return " "
    
    if N//2 >= 1:
        word += bitOper(N//2)
    
    if N%2 == 0:
        word += " "
    else:
        word += "#"
        
    return word