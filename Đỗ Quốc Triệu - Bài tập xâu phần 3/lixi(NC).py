n = input()
k = int(input())
t = "".join(sorted(n,reverse=True))
kq = t[:k+1]
print(kq)