# Cybersecurity_Programming_HW1
Homework 1 for CSCI 4742 Cybersecurity Programming and Analysis  

**Assignment Description**  
>1- Learn about the Caesar Cipher.  
>2- Learn about strategies to brute-force a Caesar ciphertext without having the key.  
>3- Write a program in Python that receives an input ciphertext and produces its plaintext.   
>The program must output every guess in a separate line, and ask if it looks like the correct output.
>-----
>Example input/output:  
>Input  
>```
>Enter ciphertext: 
>>> haahjr
>```
>Output (y for yes, n for no)
>```
>Is it "gzzgiq"?
>>> n
>Is it "fyyfhp"?
>> n
>....
>Is it "attack"?
>>> y
>```
>------
>4- Submit your code. Only the .py file is needed.  
>5- Use your program with the following input and respond to the following questions in the textbox.  
>Input = "Zdrxzerkzfe zj dfiv zdgfikrek kyre Befncvuxv"  
>What is the correct plaintext? Just put it in a separate line in the textbox.  
>How many guesses were made before reaching the right output? Just write the number as the second line.  
>Example output
>```
>Life is beautiful
>20
>```

Program will convert the entered phrase to lowercase, then find the most frequently occurring letter. Next it will take a list of the most frequent characters in English words (e, a, r, i, o, t, n, s, l, c, u, d, p, m, h, g, b, f, y, w, k, v, x, z, j, q) and calculate the ASCII offset between the most frequent character in the string and the character in the list, starting with the most frequent and ending with the least.  It then shifts all letters by this offset, wrapping as necessary, and prompts the user if the "decoded" message appears to be correct.  This should in theory produce the correct message in fewer attempts than a "brute-force" attack, where the letters are incremented or decremented by one each attempt.
