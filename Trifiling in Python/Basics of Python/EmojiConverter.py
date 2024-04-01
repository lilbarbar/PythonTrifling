message =  input("Enter: ") 
words = message.split(" ") #splits the string into chunks that form a list
print (words)


emojis = {
    ":)": "😀",
    ":(": "😕"

}

output = ""
for i in words:
    output += emojis.get(i, i) + " "

print (output)







#same thing just w/ a function


def insert_emojis (string):
    words = string.split (" ")
    output = ""

    for i in words:
        output += emojis.get(i, i) + " "
    
    return output


print ( insert_emojis (message))