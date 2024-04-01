import random
import math


class Player:
    
    wins = 0
    losses = 0
    ties = 0
    rings = 0
    round = 1
    tourney = 0
    in_round = True
    active = True
    r_played = 0
    p_played = 0
    s_played = 0




    def __init__ (self, name):
        self.name = name

    
    def win(self):
        self.wins += 1
    

    def lose(self):
        self.losses += 1
        self.in_round = False
    
    def champ(self):
        self.rings += 1

    def move_on (self):
        self.round += 1
    

    def new_tourney (self):
        self.tourney += 1

    

    

    def stats (self):
        print (f"Name: {self.name}")
        print (f"Games:  {(self.wins + self.losses)}")
        print (f"Wins: {self.wins}")
        print (f"Losses {self.losses}")
        print (f"Ties: {self.ties}")
        games_no_ties = self.wins + self.losses
        all_games = games_no_ties + self.ties
        if (games_no_ties == 0):
            print ("Win Percentage: 0%")
        else:
             print (f"Win Percentage: { round( self.wins/games_no_ties * 100 ) }% ")
        print (f"Rocks Played: {self.r_played}")
        print (f"Papers Played: {self.p_played}")
        print (f"Scissors Played: {self.s_played}")
        print (f"Tournaments played {self.tourney}")
        print (f"Tournaments won {self.rings}")
        if (self.tourney != 0): 
            print (f"Wins per tournament: {self.wins/self.tourney}")
        

    


    def calc_score (self):
        return (self.wins * 100) + (self.rings * 5000) - (self.losses * 25) + (20 * self.tourney)






    def legacy (self):
        self.stats()
        score = self.calc_score()
        print ("Legacy score: " + str(score))
        if (score >= 10000):
            print ("You are the Greatest Rock, Paper Scissors player Ever!!! You changed the game and will be remembered as the GOAT in convos with Michael Jordan, Lionel Messi, Tiger Woods and Tom Brady")
        elif (score >= 5000):
            print ("You are a Hall of Famer and one of the greatest Rock Paper Scissors Players Ever!!!")
        elif (score >= 1000):
            luck = random.randint (0, 5000)
            if (luck >= score):
                print ("You are a Hall of Famer and a great Rock Paper Scissors player to be remembered!")
            else:
                print ("You were not a hall of famer but you had a great career and were a great player of the game! Props to you!")
        else:
            print ("Damn...you suck not gonna lie...at least you tried.... LMAO")
        
        print ("Thank you for playing!!!!")
                


    

    
    

