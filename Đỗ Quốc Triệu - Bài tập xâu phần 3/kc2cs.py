x = input()
y = input()
a = max(x,y)
b = min(x,y)
kq = 0
for i in range(len(a)):
    kq = kq + min(int(a[i])-int(b[i]),int(b[i])+10-int(a[i]))
print(kq)