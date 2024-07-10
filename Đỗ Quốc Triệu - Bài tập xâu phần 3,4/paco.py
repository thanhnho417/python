n,k = map(int,input().split())
s = input()
mp = {}
for i in s:
    if i not in mp:
        mp[i] = 0
    mp[i] += 1
d = 0
m = 0
for i in mp:
    d += mp[i]//2
    m == mp[i]%2
ans = 2*(d//k)
m == 2*(d%k)
if m >= k:
    ans += 1
print(ans)