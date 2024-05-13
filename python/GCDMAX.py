from thuvien import ucln,bcnn
t = int(input("Nhập số nguyên dương t: "))
A = [int(k) for k in input("Nhập " + str(t) + "số cách nhau bởi dấu cách: " ).split()]
B = []
for i in range(t):
    for j in range(len(A)-1):
        while i < j:
            if ucln(i,A[j]) == ucln(i+1,A[j+1]):
                B.append(i)
print(B)