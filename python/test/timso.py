def tong(n):
    return sum(int(k) for k in str(n))

def tich(n):
    t = 1
    for i in str(n):
        t *= int(i)
    return(t)

def xuli(x,y):
    a = max(x,y)
    while True:
        if tong(a) == x and tich(a) == y:
            return(a)
        a += 1
        if a > 10**7:
            return -1

A = [int(k) for k in input().split()]
a,b = A
kq = xuli(a,b)
print(kq)