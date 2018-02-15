N = int(input())
r = 0; g = 0;  b = 0
for i in range(N):
    cost = list(map(int, input().split()))
    if i == 0:
        r += cost[0]
        g += cost[1]
        b += cost[2]
    else:
        before_r = r; before_g = g; before_b = b;
        r = min(before_g, before_b) + cost[0]
        g = min(before_r, before_b) + cost[1]
        b = min(before_r, before_g) + cost[2]

result = min(r,g,b)
print(result)