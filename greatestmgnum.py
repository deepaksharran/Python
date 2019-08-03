print("Greatest Among 3 numbers")
a=int(input("Enter no.1: "))
b=int(input("Enter no.2: "))
c=int(input("Enter no.3: "))
if a>b and a>c:
    print(a," is greatest")
elif b>c:
    print(b," is greatest")
else:
    print(c," is greatest")
