n = int(input())
A = [0] + [int(k) for k in input().split()]
T = int(input())
dapso = 0
T = float("inf")
s = [0]*(n+1)
for i in range(1,n+1): s[i] = s[i-1] + A[i]
j = 1
for i in range(1,n+1):
    while j<= n and s[j] - s[i-1] <= T: j += 1
    if dapso < j-1: dapso = j - i
print(dapso)