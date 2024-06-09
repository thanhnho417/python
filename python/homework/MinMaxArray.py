# Min Max array
n = int(input("Nhập số nguyên dương n: "))
A = list(map(int,input("Nhập dãy A gồm " + str(n) + " số: ").split()))
f,l  = min(A),max(A)
x,y = 0,0
for i in A:
    if i == f:
        x = x + 1
    if i == l:
        y = y + 1
print(f,x)
print(l,y)