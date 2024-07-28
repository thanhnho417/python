def smm(n):
    return all(i in '69' for i in str(n))

n = int(input())
c = 0
for i in range(1,n+1):
    s = 10**(i-1)
    e = 10**i
    for j in range(s,e):
        if smm(j):
            c += 1

print(c)

def luythua69(a,n):
    if n == 0: return 1
    t = luythua69(a,n//2)
    t = t*t
    if t%2 != 0:
        t = t*a
    return t

n = int(input())
print(luythua69(2,n))
