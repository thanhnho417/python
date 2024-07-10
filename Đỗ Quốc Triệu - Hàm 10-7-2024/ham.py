def is_prime(n):
    if n <= 1:
        return False
    else:
        i = 2
        while i*i <= n:
            if n%i == 0:
                return False
            i+=1
    return True

def num_prime(n):
    i = 2
    kq = []
    while n > 1:
        if n%i == 0:
            n = n/i
            kq.append(i)
        else:
            i += 1
    if len(kq) == 0:
        kq.append(n)
    return kq