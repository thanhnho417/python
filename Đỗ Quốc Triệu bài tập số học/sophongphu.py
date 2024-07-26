def kt(n):
  kq = 0
  for i in range(1,int(n**0.5)+1):
    if n%i == 0:
      kq += i
      if i*i <= n:
        kq += n//i
  if kq > 2*n:
    return True
  else: return False
L,R = map(int,input().split())
sl = 0
for i in range(L,R+1):
  if kt(i):
    sl += 1
print(sl)
