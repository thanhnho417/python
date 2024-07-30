n,k = map(int,input().split())
A = [int(i) for i in input().split()]
A = sorted(A)
print(A[k-1])