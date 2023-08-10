# find biggest digit out of three
num = int(input("Enter any three digit number\n"))
a = 0
a = num % 10  # 3
num //= 10  # 12
b = num % 10  # 2
num //= 10  # 1
c = num % 10  # 1
num //= 10  # 0

if a > b and a > c:
    print(a, "is greatest")
elif b > c:
    print(b, "is greatest")
else:
    print(c, "is greatest")