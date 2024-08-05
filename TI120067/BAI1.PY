n = int(input())
a = 0
b = 0
while len(str(n)) > 2:
    b += n%10
    n//=10
while n > 0:
    a += n%10
    n //= 10
if a == b:
    print("YES")
else: print("NO")