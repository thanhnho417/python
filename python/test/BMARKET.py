from thuvien import chiahetcuatong
A = [int(k) for k in input("Nhập y, k, n cách nhau bởi dấu cách: ").split()]
y,k,n = A
B = []
if n == y:
    print("-1")
else:
    for i in range(1,(n-y)+1):
        if chiahetcuatong(y,i,k):
            B.append(i)
    for i in B:
        print(i, end = " ")