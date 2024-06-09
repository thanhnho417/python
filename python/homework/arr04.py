# Tổng lẻ của dãy số 
n = int(input("Nhập số nguyên dương n: "))
A = list(map(int,input("Nhập dãy A gồm " + str(n) + " số: ").split()))
t = 0
for i in A:
    if i % 2 != 0:
        t = t + i
print(t)