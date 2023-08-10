'''

    *
   **
  ***
 ****
*****

'''
a=int(input("Limit for content:\n"))
for row in range(a,0,-1):
    for space in range(1,row):
        print(" ",end="")
    for col in range (a,row-1,-1):
        print("*", end="")
    print()