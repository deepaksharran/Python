str1=input("Enter a string : ")
l=list(str1)
n=len(l)
str2=""
for i in range(n):
    if i%2==0:
        str2=str2+l[i]
print(str2)        
