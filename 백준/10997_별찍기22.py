import sys

input = sys.stdin.readline

N = int(input())
star = [[" " for _ in range(4*(N-1)+1)] for _ in range(4*(N-1)+3)]


distY = 4*(N-1)+1
distX = 4*(N-1)+2
x = 0
y = 4*(N-1)

for i in range(1, 4*(N-1) + 3):
    if i%4 == 1:
        for _ in range(distY): #반복 횟수
            star[x][y] = "*"
            y -= 1
        if i == 1: distY -= 1
        else: distY -= 2
        x += 1
        y += 1

    elif i%4 == 2:
        for _ in range(distX):
            star[x][y] = "*"
            x += 1
        distX -= 2
        x -= 1
        y += 1

    elif i%4 ==3:
        for _ in range(distY):
            star[x][y] = "*"
            y += 1
        y -= 1
        x -= 1
        distY -= 2

    else:
        for _ in range(distX):
            star[x][y] = "*"
            x -= 1
        x += 1
        y -= 1
        distX -= 2

    # print("i = ", i, "x = ", x, "y = ", y)

if N == 1:
    print("*")
else:
    for i in range(4*(N-1)+3):
        if i == 1:
            print(star[i][0], end="")
        else:
            for j in range(4*(N-1)+1):
                print(star[i][j], end="")
        print()
