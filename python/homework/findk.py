# Tìm số k
n = int(input("Nhập số nguyên dương n: "))
A = list(map(int,input("Nhập dãy A gồm " + str(n) + " số: ").split()))
k = int(input("Nhập số nguyên dương k: "))
x = ""
for i in range(len(A)):
    if A[i] == k:
        x = x + str(i+1) + " "
print(x)