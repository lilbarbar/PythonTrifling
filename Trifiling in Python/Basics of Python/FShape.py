numbers = [5,2,5,2,2]

for i in numbers:
    print (i * "X")


print ("////")
print ("////")
print ("////")

for i in numbers:
    s = ""
    j = 0
    while j < i:
        s += 'X'
        j += 1
    print (s)


print ("////")
print ("////")
print ("////")

numbers = [1,1,1,1,5]
for i in numbers:
    s = ""
    j = 0
    while j < i:
        s += 'X'
        j += 1
    print (s)


print ("////")
print ("////")
print ("////")

numbers = [5,2,5,2,5]
for i in numbers:
    s = ""
    j = 0
    while j < i:
        s += 'X'
        j += 1
    print (s)
