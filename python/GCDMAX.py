from thuvien import max_gcd
t = int(input("Nhập số nguyên dương t: "))
A = [int(k) for k in input("Nhập" + " " + str(t) + " " + "số cách nhau bởi dấu cách: " ).split()]
B = []
for i in range(len(A)):
    B.append(max_gcd(A[i]))
for i in B:
    print(i)