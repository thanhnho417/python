A = [int(k) for k in input().split()]

def kt(A):
    n = len(A)
    max_l = 0
    cur_l = 0
    max_i = -1
    max_j = -1
    i = 0

    while i < n:
        if A[i] % 2 == 0:
            cur_l += 1
        else:
            if cur_l > max_l:
                max_l = cur_l
                max_j = i
                max_i = i - cur_l
            cur_l = 0
        i += 1

    if cur_l > max_l:
        max_l = cur_l
        max_j = n
        max_i = n - cur_l

    if max_i == -1 or max_j == -1:
        return []

    return A[max_i:max_j]

print(kt(A))
