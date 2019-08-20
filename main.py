#!/usr/bin/env python3

#Take in variable
#Hardcode for now
inString = "Zdrxzerkzfe zj dfiv zdgfikrek kyre Befncvuxv"

#Store number of attempts to solve
attempts = 0

inStringAs = list()

#Convert to ASCII numerical values
for i in inString:
    inStringAs.append(ord(i))

#Have a flag for solved or unsolved
solved = 0

#Main while loop: Decrement the ASCII values by 1, wrap back to z/Z if the value drops below a/A.
#Continue until the correct phrase is obtained.
while not solved:
    outString = ''
    outStringAs = list()
    for i in inStringAs:
        #Decrement by ASCII 1, unless it's a space
        if i != 32:
            i -= 1
            #Add ASCII 26 if the value is outside aphabetical bounds
            if (i < 97 and i > 90) or i < 65:
                i += 26
        #Append to the output string
        outString += chr(i)
        #And its list of ASCII equivalents
        outStringAs.append(i)
    
    #Prompt and verify the correct string is given.
    res = input("Is it \""+outString+"\"?")
    attempts += 1
    if res == 'y' or res == 'Y':
        solved = 1
    else:
        inStringAs = outStringAs[:]
print(attempts)
