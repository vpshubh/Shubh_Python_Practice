'''WAP to reverse elments in list
# [10,20,30,40,50]
#  0
#  50'''

# list_normal=[10,20,30,40,50]
# reversed_list = []
# for data in range(len(list_normal)):
#     #print("index:",data,"::",list_normal[data])
#     temp=list_normal[data]
#     list_normal[0]=list_normal[data-1]
#     list_normal[data-1]=temp

""" for i in range(1, len(list_normal)+1): 
    reversed_list.append(list_normal[-i])
print(list_normal)
print(reversed_list) """

#WAP to reverse elments in list
list1 = [10,20,30,40,50,60]

print("Before Reverse")
for i in range(len(list1)):
    print("Index:",i,"Value:",list1[i])

counter = len(list1)-1

for i in range((len(list1)//2)):
    temp = list1[i] #10
    list1[i] = list1[counter] #50
    list1[counter] = temp #10
    counter-=1

print("After Reverse")
for i in range(len(list1)):
    print("Index:",i,"Value:",list1[i])




