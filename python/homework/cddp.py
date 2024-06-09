# Cực đại địa phương
n = int(input("Nhập số nguyên dương n: "))
A = list(map(int,input("Nhập dãy A gồm " + str(n) + " số: ").split()))
t = 0
for i in range(1,len(A)-1):
    if A[i] > A[i-1] and A[i] > A[i+1]:
        t = t + 1
print(t)