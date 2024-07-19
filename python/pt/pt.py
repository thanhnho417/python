a,b,c,d,e,f = map(int,input().split())
a1 = -(a/b)
a2 = -(d/e)
a3 = c/b
a4 = f/e
if a1 != a2:
    x = (c*e-b*f)/((a*e-b*d))
    y = (c-a*x)/b
    print("%.3f"%x,"%.3f"%y)
else:
    if a3 == a4:
        print("TRUNG NHAU")
    else:
        print("SONG SONG")