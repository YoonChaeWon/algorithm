T = int(input())

test=[]
for i in range(T):
    test.append(int(input()))
length = max(test)

cases=[1,2,4]
for i in range(3, length):
    cases.append(cases[i-3] + cases[i-2] + cases[i-1])

for i in range(T):
    t = test[i]
    print(cases[t-1])