'''

*
**
***
****
*****

'''
a=int(input("Limit for content:\n"))
for row in range(a):
    for col in range (row+1):
        print("*", end="")
    print()