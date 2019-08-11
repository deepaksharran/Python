l1=[1,3,6,78,35,55]
l2=[12,24,35,24,88,120,155]
print(l1)
print(l2)
l3=[]
for i in l1:
    for j in l2:
        if i==j:
            l3.append(i)
print(l3)
