N = int(input())
stairs=[0]
for i in range(N):
    stairs.append(int(input()))

maximum=[0, stairs[1], stairs[1] + stairs[2]]
for i in range(3, N+1):
    candi = max(maximum[i-2], maximum[i-3] + stairs[i-1])
    maximum.append(candi + stairs[i])

print(maximum[N])