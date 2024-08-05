fin = "BAI4.INP"
fout = "BAI4.OUT"

def sdx(s):
    for i in range(len(s)):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

def nhapDL(fin):
    f = open(fin,"r")
    A = [i for i in f.readlines()]
    f.close()
    return A

A = nhapDL(fin)
for i in range(1,len(A)): A[i] = A[i].replace("\n","")
B = []
for i in A[1:]:
    s = str(i)
    t = 0
    p = len(s)
    z = p - 1
    ans = 0
    while p > 0 and t < len(s):
        if s[t] == s[z]:
            x = s[t:z+1]
            if sdx(x):
                s = s.replace(x,"")
                ans += 1
            else:
                z -= 1
        t += 1
    p = len(s)
    B.append(ans)
with open(fout,"w") as f:
    for i in B:
        print(i, file = f)