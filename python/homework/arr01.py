# In ngược dãy số
n = int(input("Nhập số nguyên dương n: "))
A = [int(k) for k in input("Nhập dãy a gồm " + str(n) + " số: ").split()]
for i in reversed(A): 
    print(i, end = " ")