S = input()
T = input()
kq = 0
t = 0
for i in T:
    if i == S[t]:
        t = t + 1
        if t == len(S):
            kq += 1
            t = 0
print(kq)
    
    