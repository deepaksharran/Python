print("String Palindrome")
s=str(input("Enter a word : "))
temp=list(reversed(s))
if temp==list(s):
    print(s," is a palindrome.")
else:
    print(s," is not a palindrome.")
