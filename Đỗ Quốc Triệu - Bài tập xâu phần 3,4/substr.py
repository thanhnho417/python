n = int(input())
A = []
for i in range(n):
    s = input().strip()
    a = s[0]
    b = s[-1]
    ans = ""
    kq = -1
    for j in s[1:-1]:
        if j != a and j != b:
            ans = ans + j
        else:
            if len(ans) == 0:
                kq = -1
            else:
                kq = len(ans)
    A.append(kq)
for i in A:
    print(i)