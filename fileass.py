
'''1. Write a Python program to read an entire text file.'''

# f=open("fileass.txt","r")
# print(f.read())

'''2. Write a Python program to read the first n lines of a file.'''

# f=open("fileass.txt","r")
# for i in range(int(input())):
#     print(f.readline())

'''3. Write a Python program to append text to a file and display the text.'''

# f=open("fileass.txt","a")
# f.write("  this is a appended text")
# f1=open("fileass.txt","r")
# print(f1.read())

'''4. Write a Python program to read the last n lines of a file.''' 
# n=int(input())
# f=open("fileass.txt","r")
# a=(f.readlines())
# print(a[-n:])

'''5. Write a Python program to read a file line by line and store it into a list.'''

# l=[]
# f=open("fileass.txt","r")
# for i in f:
#     l.append(i)
# print(l)

'''6. Write a Python program to read a file line by line and store it into a string variable.'''

l="kh   "
f=open("fileass.txt","r")
for i in f:
    l+=i
print(l)

# 7. Write a program to store a matrix into a nested list. (Matrix in a text file) 
# 8. Write a python program to find the longest words in a text file.
# 9. Write a Python program to count the number of lines in a text file.
# 10. Write a Python program to count the frequency of words in a file.
# 11. Write a python program to store the names and birthdays of your friends in a text file .
# 12. Write a Python program to write a list to a file.
# 13. Write a Python program to copy the contents of a file to another file .
# 14. Write a Python program to combine each line from the first file with the corresponding line in the second file.
# 15. Write a Python program to read a random line from a file.
# 16. Write a Python program to assess if a file is closed or not.
# 17. Write a Python program to remove newline characters from a file.
# 18. Write a Python program that takes a text file as input and returns the number of words of a given text file.
# Note: Some words can be separated by a comma with no space.
# 19. Write a Python program to extract characters from various text files and put them into a list.
# 20. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
# 21. Write a Python program to create a file where all letters of the English alphabet are listed by specified number of letters on each line.
# E.g	1 A
# 	2 B
# 	3 C
# 	4 D    and so on…
 
# 22. Using names.txt , a 46K text file containing over five thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply it by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?
# 23. The nth term of the sequence of triangle numbers is given by tn = ½n(n+1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values, we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number, then we shall call the word a triangle word.
# Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?
# 24. By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom in triangle.txt a 15K text file containing a triangle with one-hundred rows.