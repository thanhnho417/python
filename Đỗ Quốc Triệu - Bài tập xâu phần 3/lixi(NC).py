n = input().strip()
k = int(input())
A = []
for i in n:
    while k > 0 and A and A[-1] < k:
        A.pop()
        k -= 1
    A.append(i)
while k > 0:
    A.pop()
    k -= 1
print("".join(A))