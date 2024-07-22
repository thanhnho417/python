p,n,k = map(int,input().split())
tien = 0
for i in range(1,n+1):
    tien += i*k
if tien > p:
    print("NO")
    print(tien-p)
else:
    print("YES")