# Check whether a character is lowercase or uppercase

ch = input("Enter a Character\n")
asciival = ord(ch)

if asciival>=65 and asciival<=91:
    print("Character is a uppercase")
elif asciival>=97 and asciival<=122:
    print("Character is lowercase")    