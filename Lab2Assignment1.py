v=float(input("Enter voltage"))
r=float(input("Enter resistance"))
i=float(v/r)
print(i)
if i<0.5:
    print("low current")
elif 0.5<=i<=2 :
    print("Normal current")
else:
    print("high currrent")
