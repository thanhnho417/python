def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return a*b//gcd(a,b)

def max_gcd(n):
    t = 0
    for a in range(1, n):
        for b in range(a+1, n+1):
            t = max(t, gcd(a, b))
    return t

def uoc_so(n):
    B = []
    for i in range(1,n+1):
        if n%i == 0:
            B.append(i)
    return B

def prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
    return True

def sprime(n):
    while n > 0:
        if prime(n) == False:
            return False
        else:
            n//=10
    return True