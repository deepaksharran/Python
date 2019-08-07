x=input("Enter comma seperated values: ").split(",")
tup=tuple(x)
tup1=()
tup=tup[:]+('100',)
tup1=tup[:3]+(40,50,60)+tup[3:]
print(tup)
print(tup1)
