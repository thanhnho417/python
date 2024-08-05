n = int(input())
A = [int(k) for k in input().split()]
i = 0
B = []
a = min(A)
if a <= 0:
    t = abs(1 - a)
for i in range(len(A)):
    if A[i] <= 0:
        B[i] += A[i] + t
    else: B[i] = A[i] - t
print(*B)