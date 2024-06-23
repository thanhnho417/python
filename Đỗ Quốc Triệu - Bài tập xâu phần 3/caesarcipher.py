n = int(input())
s = input()
k = int(input())
kq = ""
for i in s:
    if i.isalpha():
        t = k%26
        if i.isupper():
            ans = chr((ord(i) - ord('A') + t) % 26 + ord("A"))
        if i.islower():
            ans = chr((ord(i) - ord("a")+t) % 26 + ord("a"))
        kq = kq + ans
    else:
        kq = kq + i
print(kq)