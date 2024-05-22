#write a program to find the factorial of a nummber
def factorial(x):
    if x==1 or x==0:
        return 1
    else:
        return(x*factorial(x-1))
n=int(input("Enter the value of n :"))
print("factorial of the number is",factorial(n))
