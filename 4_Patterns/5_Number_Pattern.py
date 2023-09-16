'''
    5
   545
  54345
 5432345
543212345 
 5432345
  54345
   545
    5  
'''
a= int(input("Enter the limit:\n"))
for row in range(a,0,-1):
    for space in range(1,row):
        print(" ",end="")
    for col in range(a+1,row,-1):
        print(col-1,end="")
    for col in range(row,a):
        print(col+1,end="")        
    print() 
for row in range(2,a+1):
    for space in range(1,row):
        print(" ",end="")
    for col in range(a+1,row,-1):
        print(col-1,end="")
    for col in range(row,a):
        print(col+1,end="")        
    print()