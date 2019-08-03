yr=int(input("Enter a random year : "))
if yr%4==0:
    print(yr," is a leap year.")
elif yr%100==0:
    print(yr," is a leap year.")
elif yr%400==0:
    print(yr," is a leap year.")
else:
    print(yr," is not a leapyear.")
