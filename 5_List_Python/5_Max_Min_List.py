import random
student_marks=[]
size = int(input("Enter a number\n"))

for i in range(1,size+1):
    student_marks.append(random.randint(10,200))
    
print(student_marks)
# print("Type is:", type(student_marks))
    
    
min_marks=student_marks[0]
max_marks=student_marks[0]

for i in range(len(student_marks)):
    if max_marks>student_marks[i]:
        max_marks=student_marks[i]
    elif min_marks<student_marks[i]:
        min_marks=student_marks[i]
        
print("Max is:",max_marks,"\nMin is:",min_marks)   