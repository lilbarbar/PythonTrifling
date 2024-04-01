#Parameters

def greet_user(first, last): #parameters in the function + generic placeholders
    print (f"Hi {first} {last}!")
    print ("Weelcome aboard")
 




print ("Start")
greet_user("John", "Smith") #positional arguements for first anfd second
greet_user ("Mary", "Jane") #arguements actual info for function
print ("Finish") #order matters....if Jane Mary then it will say Mary Jane

greet_user (last="Smith", first="John") #keyword arguements so we don't need to worry about order
#makes it clear whcih is first, which is second which sometimes is needed, especially for numerical values
