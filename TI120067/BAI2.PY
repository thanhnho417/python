X,Y,M = map(int,input().split())
t = min(X,Y)
z = max(X,Y)
y = 1
kq = 0
ans = 0
while kq < M:
    kq += t
x = int(kq/t)
while kq > M:
    kq -= t
    x -= 1
    if kq + y*z < M:
        kq += y
        y += 1
    else:
        kq -= t
        x -= 1
while kq+ y*z < M:
    ans = kq + z
    y += 1
y -= 1
print(ans)
