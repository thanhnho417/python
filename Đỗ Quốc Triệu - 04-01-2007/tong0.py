def subarray(a):
    n = len(a)
    s = [0]*n
    s[0] = a[0]
    for i in range(1, n):
        s[i] = s[i-1] + a[i]
    return s
A = [0] + [int(k) for k in input().split()]
s = subarray(A)
kt = False
print(s)
for i in range(len(s)):
    if s[i] == 0 or s[i] in s[:i+1]:
        kt = True
        break
if kt:
    print("YES")
else print("NO")

