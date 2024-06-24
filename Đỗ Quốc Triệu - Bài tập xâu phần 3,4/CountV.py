n = int(input())
s = input()
t = 0
count = 0
for i in s:
    if i == "D":
        t = t - 1
    if i == "U":
        t = t + 1
    if t == 0 and i == "U":
        count += 1
print(count)