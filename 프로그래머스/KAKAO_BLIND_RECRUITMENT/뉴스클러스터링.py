def solution(str1, str2):
    answer = 0
    
    str1Word = word(str1)
    str2Word = word(str2)
    
    str1Cnt = len(str1Word)
    str2Cnt = len(str2Word)
    
    if str1Cnt < str2Cnt:
        for s in str2Word:
            if s in str1Word:
                str1Word.remove(s)
    else:
        for s in str1Word:
            if s in str2Word:
                str2Word.remove(s)
    
    unionCnt = len(str1Word) + len(str2Word) # 합집합갯수
    cnt = (str1Cnt + str2Cnt) - unionCnt # 교집합갯수
    
    if unionCnt == 0:
        answer = 65536
    else:
        answer = int(cnt/unionCnt * 65536)
    
    return answer

def word(strWord):
    wordLst = []
    
    for i in range(len(strWord)-1):
        w = strWord[i]+strWord[i+1]
        if w.isalpha():
            wordLst.append(w.upper())
    
    return wordLst