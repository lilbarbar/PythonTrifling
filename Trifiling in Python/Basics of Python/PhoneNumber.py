digits = str( input ("Enter your phone number: ") )
words = ""
for i in digits:
    if i == "1":
        words += "one "
    elif i == "2":
        words += "two "
    elif i == "3":
        words += "three "
    elif i == "4":
        words += "four "
    elif i == "5":
        words += "five "
    elif i == "6":
        words += "six "
    elif i == "7":
        words += "seven "
    elif i == "8":
        words += "eight "
    elif i == "0":
        words += "zero "
    else:
        words += "nine "

print (words)




digits = str( input ("Enter your phoe number: ") )
words = ""



converter = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"

}

for i in digits:
    words += converter.get(i, "?") + " "
print (words)