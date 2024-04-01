class Person:
    def __init__ (self, name):
        self.name = name
    
    def talk (self):
        print ("Hi, my name is " + str(self.name))
        
    


bob = Person("Bob")
print( bob.name )
bob.talk()


tom = Person ("Tom")
print (tom.name)
tom.talk()