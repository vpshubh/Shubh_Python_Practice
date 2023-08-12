'''WAP to get sum of list items 
list = [1,2,3,4,5,6,7,8,9]'''

#list_item=[1,2,3,4,5,6,7,8,9]

a=int(input("What is the limit?\n"))
new_list=[]
#data= int(input("Enter the integer number:\n"))
for index in range(a):
    print("Enter the integer number:")
    data= int(input())
    new_list.append(data)
    
sum=0
for index in range(len(new_list)):
    sum=sum+new_list[index]
print("Elements in the list have sum:",sum)