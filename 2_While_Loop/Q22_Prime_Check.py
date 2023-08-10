'''Q.51 Write a program that accepts a number from user and 
check given number is prime number or not.'''
a = int(input("Enter the number:\n"))  
f = 0
i = 2
while i <= a / 2:
    if a % i == 0:
        f=1
    i+=1   
if f==0:
    print(a,"is a PRIME number")
else:
    print(a,"is not a PRIME number")