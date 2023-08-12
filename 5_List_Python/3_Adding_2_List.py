'''WAP to reverse elments in list
# [10,20,30,40,50]
#  0
#  50'''

list_normal=[10,20,30,40,50]
reversed_list = []
for i in range(1, len(list_normal)+1): 
    reversed_list.append(list_normal[-i])
print(list_normal)
print(reversed_list)

third_list= list_normal+reversed_list
print(third_list)

