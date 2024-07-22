a,b,c = map(int,input().split())
n = int(input())
A,B = [],[]
for i in range(n):
    x,y = map(int,input().split())
    kq = a*x + b*y + c
    if kq == 0:
        A.append("YES")
    else:
        A.append("NO")
    B.append(kq)
if A[0] == "YES" and A[-1] == "YES":
    print("THUOC")
elif A[0] == "NO" and A[-1] == "NO":
    if B[0] > 0  and B[1] > 0:
        print("CUNG PHIA")
    else:
        print("KHAC PHIA")
else:
    print("NO")