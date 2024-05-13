def ucln(a,b):
    if b == 0:
        return A
    return ucln(b,a%b)

t = int(input("Nhập số nguyên dương t: "))
A = [int(k) for k in input("Nhập " + str(t) + "số cách nhau bởi dấu cách: " )]
