n = int(input())
dem = [0]*10
for i in range(1,n+1):
  for j in range(str(i)):
    dem[int(i)] += 1
for k in range(10):
  if dem[i]:
    print(i,":",dem[i])
