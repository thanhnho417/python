fin = "GCDMAX.inp"
fout = "GCDMAX.out"
def ghiDL(fin):
    f = open(fin,"r", encoding="UTF-8")
    A = [int(i) for i in f.readlines()]
    f.close()
    return A

def xuli(A):
    B = A[1:]
    for i in B:
        for j in range(1,i+1):
            for k in range(i+1,
        