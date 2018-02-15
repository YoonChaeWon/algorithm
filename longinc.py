N = int(input())
A = list(map(int, input().split()))
DP=[]
dpmax=0
for i in range(N):
    maxlen = 0
    for j in range(i):
        if A[i] > A[j] and DP[j] >= maxlen:
            maxlen = DP[j]
    DP.append(maxlen+1)
    if DP[i] > dpmax:
        dpmax = DP[i]
print(dpmax)
