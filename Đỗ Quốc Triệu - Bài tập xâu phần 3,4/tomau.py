n = int(input())
A = []
for i in range(n):
    x = int(input())
    s = input()
    while i < len(s)-1:
        if s[i] == s[i+1]:
            s = s[:i]+s[i+2:]
            if i > 0:
                i -= 1
        else:
            i += 1
    if len(s) == 1 and s == "W":
        A.append("YES")
    elif len(s) == 1:
        A.append("NO")
    elif s.startswith("BW") or s.startswith("RW"):
        A.append("NO")
    elif s.endswith("WB") or s.endswith("WR"):
        A.append("NO")
    elif "WRW" in s or "WBW" in s:
        A.append("NO")
    else:
        A.append("YES")
for i in A:
    print(i)