'''Q.41 Write a program that accepts a number from user and check given number is palindrome number
or not.'''

a=int(input("Enter the number:\n"))
n=a
rev=0
while a>0:
    r=a%10
    rev=(rev*10)+r
    a= a//10
print("Reversed number is: ",rev)
if rev==n:
    print(n,"is a Palindrome Number")
else:
    print(n,"is not a Palindrome Number")