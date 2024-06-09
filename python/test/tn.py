n = int(input("Nhập số học sinh: "))
y = [int(k) for k in input("Nhập số ngày trực nhật của mỗi học sinh: ").split()]
def ucln(a,b):
    if b == 0:
        return a
    return ucln(b,a%b)

def bcnn(a,b):
    return a*b//ucln(a,b)

def ngaytieptheo(a,b):
    ht = b[0]
    for i in range(1,a):
        ht = bcnn(ht,b[i])
    return ht

def demsongay(a,b,ht):
    ngay = [ht//b[i] for i in range(a)]
    return ngay

ht = ngaytieptheo(n,y)
ngay = demsongay(n,y,ht)
print(ht)
print(*ngay)