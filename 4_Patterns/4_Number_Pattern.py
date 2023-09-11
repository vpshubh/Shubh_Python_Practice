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
    for col in range(5,row-1,-1):
        print(col, end=" ")
    for col in range(5,row,-1):
        print(col, end=" ")
    print() 