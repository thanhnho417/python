A = [0] + [int(k) for k in input().split()]
n = int(input())
def subarray(a):
    n = len(a)
    S = [0]*n
    S[0] = a[0]
    for i in range(1,n): S[i] = S[i-1] + a[i]
    return S
B = []
S = subarray(A)
u,v = 0,0
d = {}
for i in range(1,len(S)):
    for j in range(i, len(S)):
        k = S[j] - S[i-1]
        if k == n:
            B.append([i,j])
            if k not in d:
                d[k] = 1
            else: d[k] += 1
print(B[0])
print(d)        
