n = int(input())
s = input()
sp = "ueoai"
t = 0
vl = 0
for i in s:
    if i in sp:
        t = t + 1
    if not i in sp:
        if t > vl:
            vl = t
        else:
            t = 0
print(vl)