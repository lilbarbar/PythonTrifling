#DRY --> Don't Repeat Yourself




#inherits from parent class



class Mammal:
    def walk(self):
        print ("walk")


class Dog (Mammal):
    def bark(self):
        print ("WOOF")
    pass
    



class Cat (Mammal):
    def meow(self):
        print ("Meow")
    pass




dog1 = Dog()
cat1 = Cat()
dog1.walk()
dog1.bark()
cat1.walk()
cat1.meow()