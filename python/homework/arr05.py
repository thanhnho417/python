# Vị trí và giá trị lớn nhất 
n = int(input("Nhập số nguyên dương n: "))
A = list(map(int,input("Nhập dãy A gồm " + str(n) + " số: ").split()))
x = max(A)
print(x)
print(A.index(x) + 1)