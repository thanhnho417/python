from thuvien import uoc_so

n = int(input("Nhập số nguyên dương n: "))
A = [int(k) for k in input("Nhập" + " " + str(n) + " " + "số cách nhau bởi dấu cách: " ).split()]
for i in range(len(A)):
    if len(uoc_so(A[i])) == 3:
        print("YES")
    else:
        print("NO")