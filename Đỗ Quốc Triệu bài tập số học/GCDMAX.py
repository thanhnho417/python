fin = "GCDMAX.inp"
fout = "GCDMAX.out"

def nhapDL(fin):
    with open(fin, "r", encoding="UTF-8") as f:
        A = [int(line.strip()) for line in f.readlines()]
        A = A[1:]
    return A

def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def xuli(A):
    B = []
    for i in A:
        h = 0
        for j in range(1,i):
            for k in range(j+1,i+1):
                h = max(h,GCD(j,k))
        B.append(h)
    return B

def ghiDL(fout, B):
    with open(fout, "w", encoding="UTF-8") as f:
        for i in B:
            print(i, file=f)

A = nhapDL(fin)
B = xuli(A)
ghiDL(fout, B)
