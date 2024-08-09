A = [int(k) for k in input().split()]
imax = 0
jmax = 0
lenmax = 0
i = 0
while i < len(A):
    j = i + 1
    while j < len(A) and A[j-1] < A[j]:
        j += 1
    
    if j - i > lenmax:
        imax = i
        jmax = j
        lenmax = j - i
    
    i = j
print(*A[imax:jmax])
