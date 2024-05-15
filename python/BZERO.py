from thuvien import giaithua
n = int(input("Nhập số nguyên n: "))
a = str(giaithua(n))
t = "0"
c = 0
for i in reversed(range(len(a))):
    if a[i] == t:
        c += 1
    if a[i] != t:
        break
print(c)