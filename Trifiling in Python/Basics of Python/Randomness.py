import random #built in module in python libraries

for i in range(3):
    print( random.random() )#generates a random float value between 0 and 1




for i in range(3):
    print( random.randint(10,20) )#generates a random INt between 2 valuyes




members = ["John", "Bobby", "Uzi"]

leader = random.choice(members) #chooses a random element in the list
print (leader)