n = int(input())
s = input().strip()
ans = ""
def kt(s):
    temp = 0
    ans = ""
    for i in s:
        if i not in ans:
            temp += 1
            ans+= i
    for i in s:
        if i*2 in s or temp == 3:
            return False
            break
    return True
for i in s:
    k = s.replace(i,"")
    if kt(k):
        if len(k) > len(ans):
            ans = k
print(ans)