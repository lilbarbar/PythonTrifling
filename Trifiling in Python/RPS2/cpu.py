import random

from npc import NPC



class Computer:
    
    billy =  NPC ("Billy", 10, 50, 40)
    johan =  NPC ("Johan", 33, 33, 33)
    miles =  NPC ("Miles", 25, 50, 25)
    symere =  NPC ("Symere", 40, 40, 20)
    angela =  NPC ("Angela", 30, 10, 60)
    philip =  NPC ("Philip", 35, 30, 35)
    gertrude =  NPC ("Gertrude", 20, 55, 25)
    neelah =  NPC ("Billy", 46, 38, 16)
    temna =  NPC ("Temna", 33, 33, 33)
    timothy =  NPC ("Timothy", 50, 10, 40)
    sarah =  NPC ("Sarah", 50, 50, 00)





    options = ["rock", "paper", "scissors"]

    names = [billy, johan, miles, symere, angela, philip, gertrude, neelah, temna, timothy, sarah]

    og = [billy, johan, miles, symere, angela, philip, gertrude, neelah, temna, timothy, sarah]

    def c_select (self):
        
        return random.choice(self.options)
    

    def name_select (self):
        opp = random.choice (self.names)
        self.names.remove(opp)
        return opp

    