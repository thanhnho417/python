n = int(input())
def giaithua(n):
    if n == 0:
        return 1
    else:
        return n * giaithua(n - 1)

k = giaithua(n)
c = 0
t = 0
while c == 0:
    if k%10 != 0:
        c += 1
    else:
        k//=10
        t += 1
print(t)