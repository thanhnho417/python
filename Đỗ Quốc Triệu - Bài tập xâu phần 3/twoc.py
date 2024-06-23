s = input()
t = input()
while t in s:
    k = s.index(t)
    s = s[:k]+ s[k+len(t):]
print(s)