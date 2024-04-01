i = 1 #while loops
while i <= 100:
    print (i)
    i += 1
print ("Done")

#can multiply a symbol in a for loop as well

i = 1
while i <= 10:
    print (i * ":) ")
    i+=1

numbers = [1,2,3,4,5]

#while loop printing every number
#break ---> break ends the loop
i = 0
while i < len(numbers):
    print (numbers[i])
    i += 1





#for loops

print ("/////")


for item in numbers:
    print (item)


print ("///")

for item in 'Python':
    print (item)






    #Nested loops
   


    #used nested loop for coordinates easily

for x in range(4):
    for y in range(3):
        print (f"({x},{y})")