# Học sinh ham chơi
n = int(input("Nhập số nguyên dương n: "))
A = list(map(int, input(f"Nhập dãy A gồm {n} số: ").split()))
m = 0
for i in range(n-1):
    s = A[i]
    if s > m:
        m = s
print(m)