print("Enter Date in YYYY,MM,DD format /n Same month and year")
x=input("Enter date 1(start) : ").split(",")
y=input("Enter date 2 (end) : ").split(",")
d1=list(x)
d2=list(y)
if d1[1]==d2[1]:#same month
    days=int(d2[2])-int(d1[2])
    print("No. of days are ",days)
else :
    print("Check inputs are of same month and year")
