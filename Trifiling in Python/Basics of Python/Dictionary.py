#Name: John Smith
#Email: john@hmail.com
#Phone: 1234




#Dictionary ex.


#each key in a dictionary should be unique
#every word listed once
customer = {
    "Name": "John Smith",
    "age": 30,
    "is_verified": True



}


#can only print keys in dictionary CASE SENSITIVE
print(customer ["Name"])
customer["Name"] = "Billy"
print (customer.get("Name")) 
print (customer.get("birthdate")) #returns none as not a part of dictionary
print (customer.get("birthdate", "June 20")) #second parameter is the default return assuming the dictionary does not have a key value for the first parameter