#construcotrs

class Point:
    #CLASS METHODS

    def __init__ (self, x, y): #construcotr init for initial  __init__(self)
        #self is like this
        self.x = x
        self.y = y



    def move(self):
        print ("move")
    

    def draw(self):
        print ("draw")
    




point = Point (10, 20)
print (point.x)
print (point.y)

point.x = 11
print (point.x)



