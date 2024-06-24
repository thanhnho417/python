n,k = map(int,input().split())
h = str(n)*k
while len(h) > 1:
    ans = 0
    for i in h:
        ans += int(i)
    h = str(ans)
print(h)