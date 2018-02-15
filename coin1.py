nk=list(map(int, input().split()))
n = nk[0]; k = nk[1]
coin=[0]
for i in range(n):
    coin.append(int(input()))
NUM=[1]
for i in range(k):
    NUM.append(0)

for i in range(1, len(coin)):
    for j in range(coin[i], k+1):
        NUM[j] += NUM[j-coin[i]]
print(NUM[k])