'''Q.2 Write a program accepts a number from user and check given number is even or odd.'''
a=int(input("Enter the number:\n"))
res=a%2
if res==0 :
    print("Given number is Even.\n")
else:
    print("Given number is Odd.\n")