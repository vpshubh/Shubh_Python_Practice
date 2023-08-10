'''Q.47 Write a program to calculate sum of squares of n natural number'''
a=int(input("Enter the limit:\n"))
i=1
sqsum = 0
while i<=a:
    sqsum += i ** 2
    i+=1 
print("The sum of squares of the first", a, "natural numbers is:", sqsum)

 