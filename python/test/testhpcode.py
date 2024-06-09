def hettiet(k):
    k = int(input("Nhap so tiet: "))
    h = 7
    c = 0
    for i in range(1, k + 1):
        if i % 2 == 0:
            c = c + 50
        else:
            c = c + 55
        while c >= 60:
            h = h + 1
            c = c - 60
    if k % 2 == 0:
        c = c - 5
    else:
        c = c - 10
    print(h, c)

def goidienthoai(A):
    A = [int(k) for k in input().split()]
    a, x, b, y, k = A
    t = a + b
    c = 0
    if t <= k:
        print("0")
    else:
        t = t - k
        if t <= a:
            c += t * x
        else:
            c += a * x
            t = t - a
            if t <= b:
                c += t * y
            else:
                c += b * y + (t - b) * y
    print(c)