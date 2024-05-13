def ucln(a,b):
    if b == 0:
        return a
    return ucln(b,a%b)

def bcnn(a,b):
    return a*b//ucln(a,b)