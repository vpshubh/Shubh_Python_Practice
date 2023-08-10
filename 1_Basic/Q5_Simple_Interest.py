#Q.3 Write a program to find out simple interest (SI).
ppl= float(input("Principle Amount: "))
roi=float(input("Rate of Interest %: "))
tim=int(input("Time Years: "))
si=(ppl*roi*tim)/100
print("Simple Interest: ",si)