def uoc(n):
    if n == 1:
        return 1
    t = []
    for i in range(1,n+1):
        if n%i == 0:
            t.append(i)
    return t

def snt(n):
    if n <= 1:
        return False
    i = 2
    while i*2 <= n:
        if n%i == 0:
            return False
        i += 1
    return True

n = int(input())
ans = ""
t = uoc(n)
for i in t:
    if snt(i):
        ans += str(i) + " "

print(ans)