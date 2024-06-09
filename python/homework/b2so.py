# Bộ 2 số
n = int(input("Nhập số nguyên dương n: "))
A = list(map(int,input("Nhập dãy A gồm " + str(n) + " số: ").split()))
t = 0
for i in range(len(A)-1):
    tong = (A[i] + A[i+1])/2
    can = (A[i]*A[i+1])**0.5
    if tong > can:
        t = t + 1
print(t)