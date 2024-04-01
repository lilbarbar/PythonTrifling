import random 


class NPC:
    
    


    def __init__ (self, name, r_chance, p_chance, s_chance):
        self.name = name
        self.r_chance = r_chance
        self.p_chance = p_chance
        self.s_chance = s_chance

    def tendency (self):
        if (self.r_chance == self.p_chance and self.r_chance == self.s_chance):
            return f"{self.name} doesn't have any tendencies and just randomly chooses an option!"
        else:
            return f"{self.name} plays rock {self.r_chance}% of the time, paper {self.p_chance}% of the time and scissors {self.s_chance}% of the time."


    def choice (self):
        luck = random.randint (1,99)
        if (luck <= self.r_chance):
            return "rock"
        elif (luck <= self.r_chance + self.p_chance):
            return "paper"
        else:
            return "scissors"


