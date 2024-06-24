n,k = map(int,input().split())
s = reversed(input())
t = 0
for i in s:
    if i == i+1:
        ans = ans + 1
        
