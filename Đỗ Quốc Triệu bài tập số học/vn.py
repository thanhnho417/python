fin = "Vn.inp"
fout = "Vn.out"

def ucln(a,b):
    while b > 0:
        a,b = b, a%b
    return a

def nhapDL(fin):
    with open(fin,"r", encoding = "UTF-8") as f:
        lines = f.readlines()
    a,b = map(int,lines[0].split())
    return a,b


def ghiDL(fout,kq,n,m):
    with open(fout,"w", encoding = "UTF-8") as f:
        print(kq, file = f)
        print(int(n/kq), int(m/kq), file = f)

n,m = nhapDL(fin)
kq = ucln(n,m)
ghiDL(fout,kq,n,m)