s = input()
t = input()
while t in s:
    s = s.replace(t,"")
print(s)