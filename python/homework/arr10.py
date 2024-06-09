# Số lượng số âm số dương
n = int(input("Nhập số nguyên dương n: "))
A = list(map(int,input("Nhập dãy A gồm " + str(n) + " số: ").split()))
f,l = 0,0
for i in A:
    if i < 0:
        f = f + 1
    if i > 0:
        l = l + 1
print(f)
print(l)