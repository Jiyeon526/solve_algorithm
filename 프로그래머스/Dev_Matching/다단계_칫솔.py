node = {}
sale = {}
res = {}

def solution(enroll, referral, seller, amount):
    answer = []
    for i in range(len(enroll)):
        if referral[i] not in node:
            node[referral[i]] = []
        node[referral[i]].append(enroll[i])

    for i in range(len(seller)):
        if seller[i] not in sale:
            sale[seller[i]] = 0
        sale[seller[i]] += amount[i] * 100

    # print(node)
    # print()
    # print(sale)

    profit('-')
    # print()
    # print(res)
    
    for i in range(len(enroll)):
        answer.append(res[enroll[i]])
    return answer

def profit(nowNode):
    if nowNode not in res:
        res[nowNode] = 0

    myProfit = [sale[nowNode] if nowNode in sale else 0]
    if nowNode in node:
        for n in node[nowNode]:
            myProfit.append(profit(n))
    
    res[nowNode] = sum(myProfit)
    otherProfit = [m//10 for m in myProfit if m//10 > 0]
    # if otherProfit < 10 : otherProfit = 0
    res[nowNode] -= sum(otherProfit)

    return sum(otherProfit)