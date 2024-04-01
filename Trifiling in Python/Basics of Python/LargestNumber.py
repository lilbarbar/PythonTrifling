numbers = [6,8,2,10,5]
print (numbers)
max = numbers[0]

for i in numbers:
    if i>max:
        max = i

print (f"Max: {max}")





#using a module 

import utils

from utils import find_max


numbers = [0,1,3, 10.9, 8]
print (numbers)
print (find_max (numbers) )
print (utils.find_max(numbers))


# max()  --> a function that finds max value in a function...does not work for me though

numbers = (0,3,2)

# print (max (numbers)) 