n=int(input())
wine=[0]
for i in range(n):
    wine.append(int(input()))

M = [0]
for i in range(1, n+1):
    if i == 1: M.append(wine[1])
    elif i == 2: M.append(wine[1]+wine[2])
    else:
        M.append(max(M[i-2]+wine[i], M[i-3] + wine[i-1]+wine[i], M[i-1]))
print(max(M))