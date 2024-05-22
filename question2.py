# find if the given number is a palindrome or not?
n=input("Enter a number : ")
rev=n[::-1]
if n==rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
