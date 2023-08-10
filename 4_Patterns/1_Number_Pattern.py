'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

'''
a=0
for row in range(1,6):
    for col in range (1,row+1):
        a+=1
        print(a,end=" ")
    print()