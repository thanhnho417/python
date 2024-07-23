fin = "tn.inp"
fout = "tn.out"

def nhapDL(fin):
    with open(fin, "r", encoding="UTF-8") as f:
        lines = f.readlines()
    n = int(lines[0].strip())
    A = [int(i) for i in lines[1].strip().split()]
    return n, A

def xuli(n, A):
    k = 0
    B = []
    for i in A:
        k += i + 1
    for i in A:
        B.append(k // i)
    return k, B

def ghiDL(fout, k, B):
    with open(fout, "w", encoding="UTF-8") as f:
        print(k, file=f)
        for i in B:
            print(i, end=" ", file=f)
        print(file=f)

n, A = nhapDL(fin)
k, B = xuli(n, A)
ghiDL(fout, k, B)
