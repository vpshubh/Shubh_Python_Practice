import random                       #importing random defined library

list1 = []                             #defining the empty list spacing for inputting user defined list
size = int(input("Enter a number\n"))

for i in range(1,size+1):
    list1.append(random.randint(10,200))
    
print(list1)