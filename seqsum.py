n = int(input())
seq = list(map(int, input().split()))

max = seq[0]
for i in range(1, n):
    if(seq[i-1] > 0):
        if(seq[i-1] + seq[i] > 0):
            seq[i] += seq[i-1]
    if(seq[i] > max):
        max = seq[i]
print(max)