s = input().strip()
n = len(s)
kq = 0
def kt(l,r):
    while l >= 0 and r < n and s[l] == s[r]:
        l -= 1
        r += 1
    return r - l -1
for i in range(n):
    l1 = kt(i,i)
    l2 = kt(i,i+1)
    kq = max(kq,l1,l2)
print(kq)