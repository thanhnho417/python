def slc(x,y):
    return abs(x-y)

def slcd(x,A):
    temp = slc(A[0],A[1])
    for i in A:
        y = slc(x,i)
        if y < temp:
            temp = y
    return temp

n = int(input())
A = [int(k) for k in input().split()]
t = 0
for i in range(len(A)):
    x = A[0]
    A.remove(x)
    t += slcd(x,A)
    A.append(x)
print(t)