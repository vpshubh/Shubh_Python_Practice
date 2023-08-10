'''Q.12 Write a program for generating electricity Bill Accept last month unit and current month unit from
user, then calculate and print bill amount according to following condition
0-150 charges 4 rs/unit
151-300 charges 6 rs/unit
301-500 8rs/unit
>500 charges 10rs/unit

'''
last = float(input("Enter the units consumed in the last month:\n"))
current = float(input("Enter the units consumed in the current month:\n"))
total = current - last
if total <= 150:
    bill = total * 4
elif 150 < total <= 300:
    bill = 150 * 4 + (total - 150) * 6
elif 300 < total <= 500:
    bill = 150 * 4 + 150 * 6 + (total - 300) * 8
else:
    bill = 150 * 4 + 150 * 6 + 200 * 8 + (total - 500) * 10
    
print("Your electricity bill amount is:", bill, "rs")
