y, k, n = map(int, input().strip().split())
h = 0
i = 1
A = []
while h <= n:
    h = k * i
    if h - y > 0 and h <= n:
        A.append(h - y)
    i += 1

if len(A) == 0:
    print("-1")
else:
    print(*A)
