# find biggest digit out of three
a=int(input("Enter the number"))
rem=0
brk=0
max=0
for i in range(1,a):
    if a>0:
        rem=a%10
        a=a//10
if rem>max:
    print(rem)