def maxsumarray(a,M):
    n = len(a)
    i,j = 0,0
    smax = a[0]
    imax,jmax = 0,0
    s = 0
    while i<n:
        while j<n and s+a[j] <= M:
            s = s+a[j]
            j += 1
        if s >= smax and (j-i) > (jmax-imax):
            smax = s
            imax = i
            jmax = j-1
        s = s-a[i]
        i += 1
    return smax, imax, jmax
n = int(input())
A = [int(k) for k in input().split()]
smax,imax,jmax = maxsumarray(A,n)
x = A[imax:jmax+1]
print(x)
print(smax)