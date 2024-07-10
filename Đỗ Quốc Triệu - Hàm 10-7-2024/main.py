from ham import num_prime
n = int(input())
kq = set(num_prime(n))
ans = list(kq)
print(*ans)