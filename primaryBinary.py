N = int(input())

pb=[1,1]
for i in range(2,N):
    pb.append(pb[i-1] + pb[i-2])
print(pb[N-1])