#Số lượng và tổng dãy số 
n = int(input("Nhập số nguyên dương n: "))
A = [int(k) for k in input("Nhập dãy a gồm " + str(n) + " số: ").split()]
c = 0
t = 0
for i in range(len(A)-1):
    if A[i] > A[len(A)-1]:
        c = c + 1
        t = t + A[i]
print(c)
print(t)