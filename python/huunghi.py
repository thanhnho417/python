A = []
for i in range(10, 101):
    t = 0
    for j in range(1, i):
        if i % j == 0:
            t += j
    if t == i:
        A.append(i)
for i in A:
    print(i)
