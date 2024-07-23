q = int(input())
A = []

def kochiahet(n, k):
    t = 0
    i = 1
    while t < k:
        if i % n != 0:
            t += 1
        i += 1
    return i - 1 

for _ in range(q):
    n, k = map(int, input().split())
    t = kochiahet(n, k)
    A.append(t)

for result in A:
    print(result)

