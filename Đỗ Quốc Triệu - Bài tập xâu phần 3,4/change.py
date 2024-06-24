s = input()
n = "12345678"
for i in s:
    if i == "L":
        n = n + n[0]
        n = n[1:]
    if i == "R":
        n = n[len(n)-1] + n
        n = n[:len(n)-1]
print(n)