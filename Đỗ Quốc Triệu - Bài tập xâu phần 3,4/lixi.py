n = input().strip()
k = int(input())
ans = ""
for i in n:
    while ans != "" and k > 0 and i > ans[-1]:
        ans = ans[:-1]
        k -= 1
    ans = ans + i
while k > 0:
    ans = ans[:-1]
print(ans)