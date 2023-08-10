'''Q.11 Write a program that accepts five subjects’ marks from user and 
calculate the total marks then calculate
Percentage Display message according to following condition.
Percentage >=60 then print message Grade A
Percentage >=50 then print message Grade B
Percentage >= 40 then print message Grade C
Percentage < 40 then print message Grade D
'''
hin=int(input("Marks for Hindi:\n"))
eng=int(input("Marks for English:\n"))
mat=int(input("Marks for Mathematics:\n"))
sst=int(input("Marks for Social Science:\n"))
sci=int(input("Marks for Science:\n"))
tot=hin+eng+mat+sst+sci
per=(tot/500)*100
if per>=60:
    print("Grade A", per,"%")
elif per>=50:
    print("Grade B", per,"%")
elif per>=40:
    print("Grade C", per,"%")
else :
    print("Grade D", per,"%")