'''

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

'''
a=int(input("Limit for content:\n"))
for row in range(a,0,-1):
    for space in range(1,row):
        print(" ",end="")
    for col in range (a,row-1,-1):
        print("*", end="")
    for col in range (a-1,row-1,-1):
        print("*", end="")
    print()
for row in range(2,a+2):
    for space in range(1,row):
        print(" ",end="")
    for col in range (a,row-1,-1):
        print("*", end="")
    for col in range (a-1,row-1,-1):
        print("*", end="")
    print()
