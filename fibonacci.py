zero = [1, 0, 1]
one = [0, 1, 1]

def fib(n):
    length = len(n)
    if length <= n:
        for i in range(length, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print("%d %d" % (zero[n], one[n]))

num = int(input())
for i in range(num):
    fib(int(input()))
