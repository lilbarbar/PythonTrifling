
#DEALS WITH ERRORS, TRY THIS THEN PRINT ERROR w/o breaking code


#comments w/ #
try:
    age = int( input("Age: "))
    income = 20000
    risk = income/age
    print (age)

    

except ValueError: 
    print ("Invalid value")

except ZeroDivisionError:
    print ("Age cannot be 0")









print ("hello")