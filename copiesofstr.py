def copystr(s,n):
    res=""
    for i in range(n):
        res=res+s
    return res
s=input("Enter a string: ")
n=int(input("Enter a no. of copies to be made: "))
print(copystr(s,n))
