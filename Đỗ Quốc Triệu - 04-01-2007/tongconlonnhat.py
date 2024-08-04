a = [0]+[int(k) for k in input().split()]
def subarray(a):
    n = len(a)
    s = [0]*(n)
    for i in range(1,n): s[i] = s[i-1] + a[i]
    return s
    
def max_subarray(a):
    s = subarray(a)
    Smax = s[0]
    imax,jmax = 0,0
    for i in range(1,len(a)):
        for j in range(i,len(a)):
            if Smax < s[j] - s[i-1]:
                imax = i
                jmax = j
    return Smax,imax,jmax

Smax,imax,jmax = max_subarray(a)
print(Smax)
for i in range(imax,jmax+1):
    print(a[i], end = " ")