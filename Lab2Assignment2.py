h=float(input("Enter Hardness"))
c=float(input("Enter Carbon content"))
t=float(input("Enter Tensile strength"))
if h>50 and c<0.7 and t>5600:
    print("Grade 10")
elif h>50 and c<0.7:
    print("Grade 9")
elif c<0.7 and t>5600:
    print("Grade 8")
elif h>50  and t>5600:
    print("Grade 7")
elif h>50 or c<0.7 or t>5600:
    print("Grade 6")
else:
    print("Grade 5")
