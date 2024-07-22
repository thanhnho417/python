n = int(input())
c = 0
t = 10000
while n != 1 and t < 10000:
    if n % 6 == 0:
        n //= 6
    else:
        n = 3 * n
    c += 1
if n == 1:
    print(c)
else:
    print(-1)