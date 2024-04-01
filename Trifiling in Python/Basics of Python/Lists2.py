

numbers = [1,2,3,4,5]
print (1 in numbers) #boolean expression, returns boolean value whether it is in the list or not
print (10 in numbers) 




print (len(numbers)) #returns length of list




numbers = [5,2,1,6,7]

numbers.pop() #removes the last item in a list
print (numbers)


print ( numbers.index(5) ) #returns index of first appearance of 5 in the list

#print ( numbers.index(15) ) 
# #returns index of first appearance of 5 in the list, if not in the list, then breaks code


numbers = [5,2,5,6,7]

print ( numbers.count(5) ) #returns number of certain value in the list, returns 2 here since there are 2 5's

numbers.sort() #sorts list in ascending order, no parameters, returns nothing
print (numbers)

numbers.reverse() #reverse the list

print (numbers)


numbers.clear()
print (numbers)












old = [1,2,3]
new = old.copy()
#makes a copy of the list, you can edit numbers, without changing numbers2
#.copy()
old.append(4)

print (new)