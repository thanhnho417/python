# Vị trí và giá trị nhỏ nhất 
n = int(input("Nhập số nguyên dương n: "))
A = list(map(int,input("Nhập dãy A gồm " + str(n) + " số: ").split()))
x = min(A)
print(x)
B = [i for i in range(len(A)) if A[i] == x]
for i in B:
    print(i+1, end = " ")