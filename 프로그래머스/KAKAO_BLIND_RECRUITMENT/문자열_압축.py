def solution(s):
    answer = len(s)
    s += "0"
    
    for i in range(1, len(s)):
        compStr = s[0:i]
        idx = i
        newStr = ""
        cnt = 1

        while idx < len(s):
            nowStr = s[idx:idx+i]
  
            if compStr != nowStr:
                newStr += str(cnt) + compStr
                if idx + i > len(s) - 1:
                    compStr = s[idx:len(s) - 1]
                else:
                    compStr = s[idx:idx+i]
                cnt = 1
    
            else:
                cnt += 1
            idx += i
       
        newTempStr = ""
        for n in range(len(newStr)):
            if newStr[n].isalpha(): 
                newTempStr += newStr[n]
            else:
                if newStr[n] == "1" and (newStr[n-1].isdigit() or newStr[n+1].isdigit()):
                    newTempStr += newStr[n]
                elif newStr[n] != "1" and newStr[n].isdigit():
                    newTempStr += newStr[n]
                    
        length = len(newTempStr)
        if len(compStr) != i:
            length += len(compStr)
        
        if answer > length:
            answer = length
     
        # print(newTempStr)
        
        
    return answer