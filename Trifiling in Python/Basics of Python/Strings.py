course = 'Python for Beginners'

print (len(course)) #prints length of characters

#strings immutable so don't change but methods acted upon strings print different versions of said string

#you can use ' if you want "s in your program and " if you want 's in your program



course.upper()   #methods is a function specific to object (string)
course.lower()


#len and print are general purpose functions not belonging to a class or objec


print (course[0]) #prints first character (first index is 0)
print (course[-1]) #prunts last character
print (course[0:3]) #prints characters 0 to 3 including 0 not including 3
print (course[2:]) #prints everything from start index to end of string 
print (course[:4]) #prints everything from the start of the string to 4 not including 4
print (course[:]) #prints everything from 0 to end of string



print ( course.upper() ) #all upper case
print (course) #prints string





print (course.find('y')) #finds index of word/character, if not there returns -1
print (course.find('Y'))
print (course.find('for'))

print (course.replace ('for', '4')) # replaces word with another word, if not there does not replace 
print (course.replace ('x', '4'))



print (course.find ('Python')) #finds index of word






print ('Python' in course) #returns true if it is in the word, otherwise returns false
print ('Bobby' in course)





course = '''

Hi John,

Here is our first email to you.

Thank you,
The support team




''' #3 quotes for long strings w/ multiple lines like emails
print (course)



name = "Jennifer"
print (name[1:-1]) #all the characters from start to the last character excluding the last character






