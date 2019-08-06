def pattern(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        print("\r")
pattern(5)
