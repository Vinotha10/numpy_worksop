#write a program to find the sum of digits of a given number'
n=int(input("Enter a number : "))
sum=0
while (n!=0):
    sum+=n%10
    n=n//10
print(sum)
