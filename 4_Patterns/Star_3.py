'''

*****
****
***
**
*

'''
a=int(input("Limit for content:\n"))
for row in range(a,0,-1):
    for space in range(1,row+1):
        print("*",end="")
    # for col in range (5,1,-1):
    #     print("*", end="")
    print()