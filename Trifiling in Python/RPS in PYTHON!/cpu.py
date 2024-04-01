import random


class Computer:
    

    options = ["rock", "paper", "scissors"]

    names = ["Billy", "John", "Symere", "Angela", "Phillip", "Gertrude", "Johan", "Neelah", "Gabriel", "Isaac", "Miles", "Temna", "TJ", "Timothy", "Tessa", "Sarah", "Barbara", "Luffy", "Naruto", "Itadori"]

    og = ["Billy", "John", "Symere", "Angela", "Phillip", "Gertrude", "Johan", "Neelah", "Gabriel", "Isaac", "Miles", "Temna", "TJ", "Timothy", "Tessa", "Sarah", "Barbara", "Luffy", "Naruto", "Itadori"]

    def c_select (self):
        
        return random.choice(self.options)
    

    def name_select (self):
        opp = random.choice (self.names)
        self.names.remove(opp)
        return opp

    