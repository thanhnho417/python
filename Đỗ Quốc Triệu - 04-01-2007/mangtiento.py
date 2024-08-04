n,q = map(int,input().split())
A = [0]+[int(k) for k in input().split()]
S = [0]*(n+1)
for i in range(1,n+1): S[i] = S[i-1] + A[i]
for i in range(q):
    u,v = map(int,input().split())
    print(S[v] - S[u-1])
    