'''
In a given long string - 
The quick fox jumped over the lazy dog

a. Calculate the number of vowels
(a,e,i,o,u)
b. Calculate the number of white
spaces
c. Generate a new string where 1st
letter of each word is in caps. 
d.
Calculate
the length of the
string
'''

s1= 'The quick fox jumped over the lazy dog'
print("Type is:",type(s1))
print("String data is:",s1)
print("--------------------------")
# for i in range(len(s1)):
#     print("index:",i," Data:",s1[i])
# print("--------------------------")
# print(s1[-1])

print("--------------------------")
''' Calculate the number of vowels (a,e,i,o,u)'''
counter=0
for letter in s1:
    if letter in 'aeiou':
        counter+=1
        #print(letter,end=" ")
print("a. Number of vowels: ",counter)

print("--------------------------")

''' Calculate the number of white spaces'''
counter1=0
for whitespace in s1:
    if whitespace in ' ':
        counter1+=1
        #print(whitespace,end="*")
print("b. Number of whitespace: ",counter1)

print("--------------------------") 

''' Generate a new string where 1st letter of each word is in caps. '''

# s2=s1.upper()
# print(s2)


# print("--------------------------") 

s2=s1.title()
print("c. New capitalized each word of string: ",s2)

print("--------------------------") 

''' Calculate the length of the string'''
length_of_string= len(s1)
print("d. Length of string: ",length_of_string)

print("--------------------------") 
print("--------------------------") 