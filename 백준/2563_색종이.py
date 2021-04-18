import sys

input = sys.stdin.readline

b_size = [[0]*100 for _ in range(100)]

def area(x_1, y_1, x_2, y_2):
    for x in range(x_1, x_2):
        for y in range(y_1, y_2):
            if b_size[x][y] == 1:
                continue
            b_size[x][y] = 1
    
def count_size():
    count = 0

    for x in range(100):
        for y in range(100):
            if b_size[x][y] == 1:
                count += 1
    return count


N = int(input())

p_size = []
for i in range(N):
    p_size.append(list(map(int, input().split())))
    area(p_size[i][0], p_size[i][1], p_size[i][0]+10, p_size[i][1]+10)

print(count_size())