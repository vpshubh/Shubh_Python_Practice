'''Q.40 Write a program to find out reverse of a given number.'''

num=int(input("Enter any number\n"))
final=num
rem=0
rev=0
for i in range(1,num):
    if num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
print("Reverse number is:",rev)
if rev == final:
    print('Number is palindrome') 
else:
    print ('Not Palindromic Number')