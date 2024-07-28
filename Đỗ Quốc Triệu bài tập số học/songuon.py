def tong(n):
  kq = 0
  while n!= 0:
    kq += n%10
    n //= 10
  return kq

m = int(input())
sl = len(str(m))
kq = 0
for i in range(sl*9,9,-1):
  n = m - i
  if tong(n)+n == m:
    kq = n
    break

print(kq)
