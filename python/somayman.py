def count_lucky_numbers(n):
    count = 0
    for i in range(1, n + 1):
        count += 2 ** i
    return count

n = int(input("Nhập số nguyên dương n (1 ≤ n ≤ 55): "))
kq = count_lucky_numbers(n)
print(kq)
