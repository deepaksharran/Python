x=input("Enter comma seperated values: ").split(",")
tup=tuple(x)
s=set()
for i in tup:
    if tup.count(i)>1:
        s.add(i)
    else:
        continue
print(s)    
        
        
