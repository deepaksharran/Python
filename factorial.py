print("FACTORIAL")
num=int(input("Enter a Number: "))
fact=1
if num<0:
    print("Factorial doesn't exist")
elif num==0:
    print("The factorial of %d is %d."%(num,1))
else:
    for i in range(1,num+1):
        fact*=i
    print("The factorial of %d is %d."%(num,fact))    
