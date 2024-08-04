A = [int(k) for k in input().split()]
B = [int(i) for i in input().split()]
k = int(input())
max_sum = 0
cur_sum = 0
max_i = -1
max_j = -1

i = 0
while i < len(A):
    j = 0
    while j < len(B):
        if A[i] + B[j] < k:
            if A[i] + B[j] > max_sum:
                cur_sum = max_sum
                max_sum = A[i] + B[j]
                max_i = i
                max_j = j  
            elif A[i] + B[j] > cur_sum:
                cur_sum = A[i] + B[j]
        j += 1
    i += 1
if max_i != -1 and max_j != -1:
    print(A[max_i], B[max_j])
else:
    print("None")
