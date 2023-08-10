'''Q.42 Write a program that accepts a number from user and check given number is Armstrong number or not.'''

a=int(input("Enter the number:\n"))
n=a
final=n
count=0 
while a != 0:
    a //= 10
    count += 1
#print("Number of digits by user: ", count)
    sum=0
while n>0:
    r= n%10
    #print(r)
    sum = sum + (r**count)
    n//=10
#print(sum)
if sum==final:
    print(final,"is an Armstrong Number")
else:
    print(final,"is not an Armstrong Number")