def uoc(n):
    if n == 1:
        return 1
    t = 0
    for i in range(1,n):
        if n%i == 0:
            t += i
    return t

n = int(input())
if n == uoc(n):
    print("YES")
else: print("NO")