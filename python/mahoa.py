def mahoa(n,a):
    c = ""
    b = a.lower()
    for i in range(len(b)):
        t = ord(b[i])
        d = t
        d = d + n
        c = c + chr(d)
    print("Kết quả: ",c)

def giaima(n,a):
    c = ""
    b = a.lower()
    for i in range(len(b)):
        t = ord(b[i])
        d = t
        d = d - n
        c = c + chr(d)
    print("Kết quả: ",c)

n = int(input("Nhập số k bất kì: "))
a = input("Nhập xâu bất kì: ")
i = int(input("Bạn muốn làm gì:  1: Mã hóa  2: Giải mã "))
if i == 1:
    mahoa(n,a)
if i == 2:
    giaima(n,a)