l=[12,24,35,24,88,120,155]
for i in l:
    if i%5==0 and i%7==0:
        l.remove(i)
print(l)        
