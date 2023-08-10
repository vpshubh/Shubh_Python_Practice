'''
    1
   12
  123
 1234
12345

'''
for row in range(5,0,-1):
    for col in range(1,row):
        print(" ",end=" ")
    for col in range(1,7-row):
        print(col, end=" ")
    print()
        