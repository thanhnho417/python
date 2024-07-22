fin = "SPRIME.INP"
fout = "SPRIME.OUT"
def snt(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
def nhapDL(fin):
    with open(fin, "r", encoding="UTF-8") as f:
        lines = f.readlines()
    a, b = map(int, lines[0].split())
    return a, b
def xuli(a, b):
    A = []
    for i in range(a, b + 1):
        t = i
        while t > 0:
            if snt(t):
                t //= 10
            else:
                break
        if t == 0:
            A.append(i)
    return A
def ghiDL(fout, A):
    with open(fout, "w", encoding="UTF-8") as f:
        for i in A:
            print(i, file=f)
a, b = nhapDL(fin)
A = xuli(a, b)
ghiDL(fout, A)