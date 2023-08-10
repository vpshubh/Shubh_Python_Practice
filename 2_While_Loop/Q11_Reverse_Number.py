'''Q.40 Write a program to find out reverse of a given number.'''
a=int(input("Enter the number:\n"))
sum=0  
while a>0:
    r=a%10
    sum=sum*10+r
    a= a//10
print("Reversed number is: ",sum)