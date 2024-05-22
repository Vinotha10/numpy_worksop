#write a program to find if the given number is prime no or not
n=int(input("Enter a number : "))
if n <= 1:
        print("Not a prime number")
for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not a prime number")
        else :
            print("Is a prime number")
