x = int(input())
op = [0, 0, 1, 1]

def makeone(num):
    for i in range(4, num+1):
        a = op[i-1]+1
        b = 9999
        c = 9999
        if i%2 == 0:
            b = op[i//2]+1
        if i%3 == 0:
            c = op[i//3]+1
        temp = min(a,b,c)
        op.append(temp)
    return op[num]

print(makeone(x))