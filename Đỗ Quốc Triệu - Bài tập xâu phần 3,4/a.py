n = input()
k = int(input())
ans = ""
for c in n:
    while ans!="" and k>0 and c>ans[-1]: 
        ans = ans[:-1]
        k-=1
    ans=ans+c
while k>0: ans = ans[:-1]
print(ans)
