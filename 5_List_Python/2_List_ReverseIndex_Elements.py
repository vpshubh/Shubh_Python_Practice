'''WAP to reverse elments in list
# [10,20,30,40,50]
#  0
#  50'''

list_normal=[10,20,30,40,50]
reversed_list = []
# for data in range(len(list_normal)):
#     #print("index:",data,"::",list_normal[data])
#     temp=list_normal[data]
#     list_normal[0]=list_normal[data-1]
#     list_normal[data-1]=temp

for i in range(1, len(list_normal)+1): 
    reversed_list.append(list_normal[-i])
print(list_normal)
print(reversed_list)

