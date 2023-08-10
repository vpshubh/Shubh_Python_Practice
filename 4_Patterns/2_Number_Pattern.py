'''
1
23
345
4567
56789

'''
a=0 
for row in range(1,6):
    a=row
    for col in range (1,row+1):
        print(a,end="")
        a+=1
    print()