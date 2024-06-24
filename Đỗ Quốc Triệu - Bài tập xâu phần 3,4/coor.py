s = input()
x,y = 0,0
x = s.count("E")-s.count("W")
y = s.count("N") - s.count("S")
print(x,y)