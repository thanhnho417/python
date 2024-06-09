# Cập nhật danh sách
n = int(input("Nhập số nguyên dương n: "))
A = list(map(int,input("Nhập dãy A gồm " + str(n) + " số: ").split()))
for i in range(len(A)):
    if A[i] > 0:
        A[i] = 1
    if A[i] < 0:
        A[i] = -1
for i in A:
    print(i, end = " ")