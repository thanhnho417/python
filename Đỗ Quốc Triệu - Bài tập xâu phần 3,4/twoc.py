n = int(input())
s = input().strip()
ans = ""
def kt(s):
    for i in s:
        if i*2 in s:
            return False
    return True
for i in s:
    k = s.replace(i,"")
    if kt(k):
        if len(k) > len(ans):
            ans = k
print(ans)