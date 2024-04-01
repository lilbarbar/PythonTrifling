weight = input ("Enter your weight: ")
weight = float (weight)

print ("Kilograms or Pounds")
units = input ("Type K for Kilos or L for Pounds ")

if units.upper() == 'K':
    other = weight * 2.2
    print ("You weigh " + str(weight) + " kilograms and " + str(other) + " pounds!")
elif units.upper() == 'L':
    other = weight / 2.2
    print ("You weigh " + str(weight) + " pounds and " + str(other) + " kilograms!") 
else:
    print ("You failed to type a 'K' or an 'L' therefore the code broke")
    print ("I will never be able to tell you your weight in kilgrams/pounds :(")

print ("Goodbye! Have a nice day!")