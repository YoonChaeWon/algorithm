NUM=[[]]
for i in range(1, 31):
    NUM.append([0])
    for j in range(1, 31):
        if i == 1:
            NUM[i].append(j)
        elif i > j:
            NUM[i].append(0)
        elif i == j:
            NUM[i].append(1)
        else:
            NUM[i].append(NUM[i-1][j-1] + NUM[i][j-1])

T = int(input())
for i in range(T):
    nm = input().split()
    N = int(nm[0]); M = int(nm[1])
    print(NUM[N][M])