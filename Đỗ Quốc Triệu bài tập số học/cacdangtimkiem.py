def Binary_Search(a,x):
  n = len(a)
  if a[0] >= x: return 0
  if a[n-1] < x: return -1
  left = 0
  right = n-1
  while left < right:


# sử dụng hàm bitsect trong python
from bisect import bisect

def Find(a,x):
	pos = bisect(a,x)
	if pos == len(a)+1 or a[pos-1] < x: return -1
	return pos-1
a = [1,5,7,9,13,21]
p = Find(a,10)
print(p)

#Đếm số lượng phần tử bằng x trong mảng a đã sắp xếp tăng dần
def Find(a,x):
  v = bisect(a,x)
  u = bisect(a,x-1)
  return v - u
