s = input()
i = 0
while i < len(s)-1:
    if s[i] == s[i+1]:
        s = s[:i]+s[i+2:]
        if i > 0:
            i -= 1
    else:
        i += 1
if len(s) == 0:
    print("Empty string")
else:
    print(s)