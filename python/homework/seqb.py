# Dãy số B
n = int(input("Nhập số nguyên dương n: "))
A = list(map(int, input("Nhập dãy A gồm " + str(n) + " số: ").split()))
B = []
for i in range(n):
    t = sum(A[:i+1])
    B.append(t)
for i in B:
    print(i, end = " ")