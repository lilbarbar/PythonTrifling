import random

class Dice:
    

    def roll (self):
        x = random.randint (1,6)
        y = random.randint (1,6)
        return (x,y)



random.uniform
dice = Dice()

for i in range (0,10):
    print ( dice.roll() )