N = int(input())

#dp[N][j] = dp[N-1][1] if L == 0
#           dp[N-1][j-1] if 0 < L < 9
#           dp[N-1][8] if L == 9

dp=[[0]]
for i in range(1, 10):
    dp[0].append(1)

for i in range(1, N):
    dp.append([])
    for j in range(10):
        if j == 0:
            dp[i].append(dp[i-1][1])
        elif j == 9:
            dp[i].append(dp[i-1][8])
        else:
            dp[i].append(dp[i-1][j-1] + dp[i-1][j+1])

print(sum(dp[N-1]) % 1000000000)
