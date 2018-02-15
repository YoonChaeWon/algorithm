n = int(input())
a = 1
b = 1
for i in range(n):
    a,b = b, a+b

print(a%10007)