def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return a*b//gcd(a,b)

def max_gcd(n):
    max_gcd_value = 0
    for a in range(1, n):
        for b in range(a+1, n+1):
            max_gcd_value = max(max_gcd_value, gcd(a, b))
    return max_gcd_value