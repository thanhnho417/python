n = int(input())
def snt(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def sdx(n):
    a = n
    k = 0
    while a > 0:
        k = k*10 + a % 10
        a //= 10
    return k

if snt(n) and snt(sdx(n)):
    print("1")
else:
    print("0")
