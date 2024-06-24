n = int(input())
s = input()
a,b,c,d = 0,0,0,0
sp = "!@#$%^&*()_+"
if any(k.isupper() for k in s):
    a = 0
if any(k.islower() for k in s):
    b = 0
if any(k.isdigit() for k in s):
    c = 0
if any(k for k in sp):
    d = 0
ans = a+b+c+d
if n + ans < 6:
    ans = 6 - (len(s)+ ans)
print(ans)