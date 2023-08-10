# Q.5 Write a program accepts 4 digits no. and display the no. in reverse order.
num = int(input("Enter the 4-digit number: "))
rev=0
rem = num%10 #4
rev = rev*10 + rem #4
num = num // 10 #123

rem = num%10 #3
rev = rev*10 + rem #4*10+3=43
num = num // 10 #12

rem = num%10 #2
rev = rev*10 + rem #43*10+1=432
num = num // 10 #1

rem = num%10 #1
rev = rev*10 + rem #432*10+1=4321
num = num // 10 #0
print("Reverse is :",rev)
