#!/usr/bin/env python3
#Gregory Wicklund
#CSCI 4742 Cybersecurity Programming and Analysis
#Homework 1: Caesar Cipher


#Take in variable
inString = input("Please enter a cipher string:\n>> ")

#Convert to lowercase
inStringLower = inString.lower()

#String with characters from most- to least-frequent occurance
charFreq = "eariotnslcudpmhgbfywkvxzjq"

#Create a dictionary to hold the counts per letter, and a list to hold "used" letters
charCount = dict()
usedChar = []

#Get unique character counts
for i in inStringLower:
    #Don't forget to exclude non-letters!
    if i not in usedChar and i.isalpha():
        charCount.update({i:inStringLower.count(i)})
        usedChar.append(i)

#Sort the frequency
charCount_sort = sorted(charCount.items(), key=lambda x: x[1], reverse=True)

#For the most frequent letter, build an array of offsets.
offsetList = []
for i in charFreq:
    offsetList.append(ord(charCount_sort[0][0]) - ord(i))

#Store number of attempts to solve
attempts = 0


inStringAs = list()
    
#Convert to ASCII numerical values
for i in inString:
    inStringAs.append(ord(i))

#Have a flag for solved or unsolved
solved = 0

#Count for position
pos = 0

#Main while loop: Decrement the ASCII values by 1, wrap back to z/Z if the value drops below a/A.
#Continue until the correct phrase is obtained.
while not solved:
    outString = ''
    outStringAs = list()
    for i in inStringAs:
        #Since there are only 7 ASCII values between 'Z' and 'a', have a check to determine if the
        #character is uppercase or lowercase
        up = chr(i).isupper()
        low = chr(i).islower()
        #Offset by the amount, provided it's a letter.
        if chr(i).isalpha():
            i -= offsetList[pos]
            
            #Add ASCII 26 if the value is below alphabetical bounds. Also verify the case.
            if (i < 97 and low) or i < 65:
                i += 26
            else:
                #Subtract ASCII 26 if the value is above alphabetical bounds.
                if i > 122 or (i > 90 and up):
                    i -= 26
        #Append to the output string
        outString += chr(i)
        #And its list of ASCII equivalents
        outStringAs.append(i)
    
    #Prompt and verify the correct string is given.
    res = input("Is it \""+outString+"\"?\n>> ")
    attempts += 1
    if res == 'y' or res == 'Y':
        solved = 1
    else:
        pos += 1
print(attempts)
