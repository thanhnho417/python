def ucln(a,b):
    while b > 0:
        a,b = b, a%b
    return a
def sodaonguoc(n):
    a = n
    k = 0
    while a > 0:
        k = k*10 + a%10
        a//=10
    return k
n = int(input())
k = 0
for i in range(1,n+1):
    b = sodaonguoc(i)
    if ucln(i,b) == 1:
        k += 1
print(k)