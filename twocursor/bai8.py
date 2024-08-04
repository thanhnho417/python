A = [int(k) for k in input().split()]

def kt(A):
    if not A:
        return []
    lm = 1
    lc = 1
    si = 0
    msi = 0

    for i in range(1, len(A)):
        if A[i] == A[i - 1]:
            lc += 1
        else:
            if lc > lm:
                lm = lc
                msi = si
            lc = 1
            si = i

    if lc > lm:
        lm = lc
        msi = si

    return A[msi:msi + lm]

print(*kt(A))
