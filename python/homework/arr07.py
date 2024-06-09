# Số nhỏ nhất lớn hơn k 
n,k = map(int,input("Nhập 2 số nguyên dương n,k: ").split())
A = list(map(int,input("Nhập dãy A gồm " + str(n) + " số: ").split()))
B = list(sorted(A))
t = 0
for i in B:
    if i > k:
        t = t + i
        break
C = [i for i in range(len(A)) if A[i] == t]
print(t)
for i in C:
    print(i+1, end = " ")