from thuvien import prime, sprime
A = [int(k) for k in input("Nhập hai số nguyên a, b: ").split()]
a,b = A
C = []
if a > b:
    print("Không hợp lệ")
else:    
    if a == b:
        if prime(a) == False:
            print("NO")
        else:
            print(a)
    else:
        for i in range(a,b+1):
            if sprime(i):
                C.append(i)
for i in C:
    print(i)