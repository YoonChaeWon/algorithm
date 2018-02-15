N = int(input())
P = list(map(int, input().split()))
P.insert(0, 0)

M = [0]
max_p = 0
for i in range(1, N+1):
    for j in range(1, i+1):
        if max_p < M[i-j] + P[j]:
            max_p = M[i-j]+P[j]
    M.append(max_p)
print(M[N])