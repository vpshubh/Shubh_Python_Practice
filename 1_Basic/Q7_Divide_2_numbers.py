'''Q.7 Write a program accepts two numbers from user and calculates first no is 
divisible by second or not.'''
a=int(input("Enter first number:\n"))
b=int(input("Enter second number:\n"))
res= a%b
if res==0 :
    print("First number is divisible by second\n")
else:
    print("First number is not divisible by second\n")