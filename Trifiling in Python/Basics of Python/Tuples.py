numbers = (1,2,3,3) #lists store a sequence of objects but immutable, and cannot be changed.....tuples are declared with paranthesiss, lists with []
#numbers[0] = 1 --> leads ti an error


num = numbers.count(3) # returns number of times said value is in the tuple (in this case 3)
print (str(num))


print(numbers.index(2)) #returns index of first occurance of element