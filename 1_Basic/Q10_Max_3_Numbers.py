'''Q.4 Write a program accepts three numbers from user and calculate biggest number out of three
numbers.'''
a=int(input("Enter the number 1st:\n"))
b=int(input("Enter the number 2nd:\n"))
c=int(input("Enter the number 3rd:\n"))

if a>b and a>c:
    print("First number is Biggest:\n",a)
elif b>c:
    print("Second number is Biggest:\n",b)
else:
    print("Third number is Biggest:\n",c)