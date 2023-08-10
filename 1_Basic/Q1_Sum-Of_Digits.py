'''
Arithmetic Assignmnet(+=,-=,*=,=,//=,**=)
'''
# Q.4 Write a program to calculate sum of digits number.(Hint:-123 is a given number then o/p=6)

num = int(input("Enter the 3 digit number: "))
sum = 0
rem = num%10 #3
#sum = sum + rem # 3
sum+=rem #3
#num = num / 10 #12.3
num=num//10 #12


rem = num%10 #2
sum+=rem #3+2=5
num=num//10 #1

rem = num%10 #1
sum+=rem #5+1 =6
num=num//10 #0
print("Sum is :",sum)   