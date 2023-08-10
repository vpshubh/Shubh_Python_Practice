# Q.6 Write a program accepts an amount in rupees (Hint Rs 4567) and find out how many currency of
# Rs 2000,500,200,100,50,20,10,5,2,1.

amt = int(input("Enter the Amount: "))
note2000 = 0
note500 = 0
note200=0
note100=0
note50=0
note20=0
note10=0
note5=0
coin2=0
coin1=0

note2000 = amt//2000 
amt = amt%2000 
print("Note2000 is:",note2000)

note500 = amt//500 
amt = amt%500 
print("Note500 is:",note500)

note200 = amt//200 
amt = amt%200 
print("Note200 is:",note200)


note100 = amt//100 
amt = amt%100 
print("Note100 is:",note100)

note50 = amt//50 
amt = amt%50 
print("Note50 is:",note50)


note20 = amt//20 
amt = amt%20 
print("Note20 is:",note20)

note10 = amt//10 
amt = amt%10 
print("Note10 is:",note10)


note5 = amt//5 
amt = amt%5 
print("Note5 is:",note5)

coin2 = amt//2 
amt = amt%2 
print("Coins2 is:",coin2)


coin1 = amt//1 
amt = amt%1 
print("Coins1 is:",coin1)

