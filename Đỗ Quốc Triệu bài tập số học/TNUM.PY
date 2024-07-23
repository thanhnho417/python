fin = "TNUM.INP"
fout = "TNUM.OUT"

def luonguoc(n):
    t = 0
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            t += 1
            if i*i < n:
                t += 1
    return t
def nhapDL(fin):
    with open(fin,"r",encoding="UTF-8") as f:
        line = f.readlines()
    A = [int(i) for i in line[1].strip().split()]
    return A

def xuli(A):
    B = []
    for i in A:
        k = luonguoc(i)
        if k == 3:
           B.append("YES")
        else: B.append("NO")
    return B

def ghiDL(fout,B):
    with open(fout,"w",encoding="UTF-8") as f:
        for i in B:
            print(i, file = f)
            
A = nhapDL(fin)
B = xuli(A)
ghiDL(fout,B)