n = int(input())
A, B = [], []
for i in range(n):
    A.append(input())
for i in A:
    if i == i[::-1]:
        B.append("YES")
    else:
        B.append("NO")
for i in B:
    print(i)
