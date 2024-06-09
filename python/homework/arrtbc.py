# Trung bình cộng dãy số
n = int(input("Nhập số nguyên dương n: "))
A = list(map(int,input("Nhập dãy A gồm " + str(n) + " số: ").split()))
x = sum(A)/len(A)
t = 0
for i in A:
    if i > x:
        t = t + i
print(t)