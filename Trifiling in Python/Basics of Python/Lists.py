import copy


names = ["Bob", "Bill", "John", "Jill"] #list with commas breaking it
print (names) #prints list
print (names[0]) #prints element at specific index in list



print (names[-1]) #prints last element in list
print (names[-2]) #prints secondlast element in list


names[2] = "Jon" #edits list

print (names)



print (names[0:3]) #prints elements from start to end (excluding end) so 0, 1 and 2
print (names)

print("/////")

numbers = [1,2,3,4,5]
print (numbers)


numbers.append(6) #adds 6 to the end of the list
print (numbers)



numbers.insert(0, -1)   #index, object for parameters
print (numbers)


numbers.remove(3) #removes value from list, (NOT THE INDEX BUT THE VALUE)
print (numbers)

numbers = numbers.clear()
 #clears list
print (numbers)
print ("###")

numbers = [0,1,3]
numbers3 = copy.deepcopy(numbers)


print (numbers3)
