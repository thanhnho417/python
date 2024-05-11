n = int(input("Nhập số nguyên n: "))
A = []
def kt(n):
    if n <= 1:
        return False
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
    return True

A.append([str(k) for k in str(n)])
d = 0
s = 0
d = str(n)[::-1]
d = int(d)
if kt(n) and kt(d):
    print("1")
else:
    print("0")
