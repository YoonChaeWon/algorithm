def findMax(S, M, length):
    m = 0
    for j in range(2, length+1):
        for i in range(2):
            if i == 0:
                candi = max(M[0][j-2], M[1][j-2], M[1][j-1]) + S[0][j]
            elif i == 1:
                candi = max(M[0][j-1], M[0][j-2], M[1][j-2]) + S[1][j]

            if m < candi:
                m = candi
            M[i].append(candi)
    return m

T = int(input())
for i in range(T):
    n = int(input())
    sticker=[];maxsum=[[0], [0]]
    for j in range(2):
        sticker.append(list(map(int, input().split())))
        sticker[j].insert(0, 0) # useless data
        maxsum[j].append(sticker[j][1])
    print(findMax(sticker, maxsum, n))