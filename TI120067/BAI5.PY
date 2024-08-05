fin = "BAI5.INP"
fout = "BAI5.OUT"
B = []
C = []
with open(fin,"r") as f:
    line = f.readlines()
n = line[0]
A = [str(i) for i in line[1:]]
B = []
C = []
D = []
for i in A:
    temp = i.split()
    a,b = temp[0],temp[1]
    x = a+""+b
    B.append([a,b])
i = 0
while i < len(B)-1:
    j = 1
    while j < len(B)-1:
        if B[0][0] < B[j][0] and B[0][1]> B[j][1]:
            C.append("1")
            break
        else:
            j += 1
    i += 1
with open(fout,"w") as f:
    for i in C:
        print(i, end = " ", file = f)