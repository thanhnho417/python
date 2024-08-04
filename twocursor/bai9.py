def kt(A):
    if not A:
        return []

    max_l = 0
    cur_l = 0
    start = 0
    max_s = 0

    for i in range(len(A)):
        if A[i] > 0:
            if cur_l == 0:
                start = i
            cur_l += 1
        else:
            if cur_l > max_l:
                max_l = cur_l
                max_s = start
            cur_l = 0

    if cur_l > max_l:
        max_l = cur_l
        max_s = start

    return A[max_s:max_s + max_l]

A = [int(k) for k in input().split()]
print(*kt(A))
