A = [int(k) for k in input().split()]
K = int(input())
A.sort()
found = False

for i in range(len(A) - 2):
    left = i + 1
    right = len(A) - 1
    while left < right:
        cur_sum = A[i] + A[left] + A[right]
        if cur_sum == K:
            print(A[i], A[left], A[right])
            found = True
            break
        elif cur_sum < K:
            left += 1
        else:
            right -= 1
    if found:
        break

if not found:
    print("None")
