'''
Q.13 Write a program to accept basic salary from user, if basic salary is between 0 and 15000 then TA is
8% of basic salary, DA is 4% of basic salary. If salary is above 15000 then TA is 10% of basic salary, DA is
5% of basic. Calculate gross salary as gs=basic salary+TA+DA?
'''
basic = float(input("Enter your basic salary: "))
if 0 < basic <= 15000:
    TA = (8/100) * basic
    DA = (4/100) * basic
else:
    TA = (10/100) * basic
    DA = (5/100) * basic
gs = basic + TA + DA
print("Your gross-salary is:", gs)
