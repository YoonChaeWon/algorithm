n = int(input())

all=[]; S=[]; parentSum=[]
for i in range(n):
    all.append(list(map(int, input().split())))
S.append(all[0][0])

for i in range(1, n):
    parentSum = S
    S = []
    for j in range(i+1):
        if j == 0: # left node
            p = parentSum[0]
        elif j == i: # right node
            p = parentSum[j-1]
        else: # inside node
            p = max(parentSum[j-1], parentSum[j])
        S.append(p + all[i][j])
print(max(S))