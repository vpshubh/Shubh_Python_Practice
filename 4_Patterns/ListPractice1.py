''' I am having the input ||a3b6|| and you have to generate the output as ||aaabbbbbb||'''

a=input("Enter the query: \n")
print(a)
b=""
i=0
while i< len(a):
    if a[i].isalpha():
        char=a[i]
        i+=1
        num=""
        while i<len(a) and a[i].isdigit():
            num+=a[i]
            i+=1
        b+=char*int(num)
print(b)
            