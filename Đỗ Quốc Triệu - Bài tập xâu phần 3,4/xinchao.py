n = int(input())
key = input()
A = [input().strip() for i in range(n)]
B = []
for i in A:
    mess = i
    x = 0
    y = len(key)
    for j in mess:
        if j == key[x]:
            x = x + 1
        if x == y:
            B.append("YES")
            break
    else:
        B.append("NO")
for i in B:
    print(i)