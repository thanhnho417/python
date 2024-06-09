# Vị trí số âm
n = int(input("Nhập số nguyên dương n: "))
A = list(map(int,input("Nhập dãy A gồm " + str(n) + " số: ").split()))
f,l = -1,-1
for i in range(len(A)):
    if A[i] < 0:
        f = i + 1
        break
for i in reversed(range(len(A))):
    if A[i] < 0:
        l = i + 1
        break
print(f,l)