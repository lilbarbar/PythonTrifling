name = input ("What is your namr? ")

while len(name) > 50 or len(name) < 3:
    if len(name) > 50:
        print ("Name can have no more than 50 characters")
        name = input ("What is your name? ")
    else:
        print ("Name must have 3 or more chcractaers")
        name = input ("What is your name? ")

print ("You have a nice name, " + name)