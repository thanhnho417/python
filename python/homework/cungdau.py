# Cùng dấu
n = int(input("Nhập số nguyên dương n: "))
A = list(map(int,input("Nhập dãy A gồm " + str(n) + " số: ").split()))
t = ""
for i in range(len(A)-1):
    if A[i] > 0 and A[i+1] > 0:
        t = t + str(A[i]) + " " + str(A[i+1])
        break
print(t)