'''Q.48 Write a program to accept n number from user and 
show how many number are even or odd.'''
n = int(input("Enter the value of n: "))
even_count = 0
odd_count = 0
i = 0
print("Enter numbers: ")
while i < n:
    num = int(input())
    if num % 2 == 0:
        even_count += 1
    else:   
        odd_count += 1
    i += 1
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
