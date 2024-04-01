import random

from player import Player

from cpu import Computer





round_dictionary = {

    1:"Round 1",
    2: "Round 2",
    3: "Semi-finals!!",
    4: "Finals!!!"




}



def reset (p,c):
    print ("What would you like to do? ")
    print ("1. Join the next tournament: ")
    print ("2. See your stats: ")
    print ("3. Retire")
    print ()
    result = str ( input ("Enter a number 1-3: ") )
    print ()
    attempts = 0
    while (result != '1') and (result != '2') and (result != '3'):
        attempts += 1
        if (attempts >= 2):
            result = str ( input ("ENTER EITHER 1, 2 or 3! LOCK IN!! ") ) 
        else:
            result =  str ( input ("Enter a number 1-3: ") )
    
    print()
    print()

    if result == "2":
        stats (p)
        print()
        print()
        print()
        reset (p,c)
    elif result == "3":
        p.active = False
        print ()
        print ()
    else:
        c.names = c.og
        p.active = True
        p.round = 1
        p.new_tourney()
        p.in_round = True
        print ()
        print ()


    



    
    


def season (p, c):
    while (p.in_round == True) and (p.round <= 4):
        initial_p_wins = p.wins
        initial_p_losses = p.losses
        opp = c.name_select()
        game (p, c, 0, opp)

        if (p.wins > initial_p_wins):
            p.move_on ()
        else:
            p.in_round = False
    if (p.round == 5):
        print ()
        print ("Congratulations! You won the tourney!")
        p.champ()






    


def game ( p,  c,  set, enemy ):
    opp = enemy

    if set == 0:
        print (round_dictionary.get(p.round, "Next Up: "))
        print (p.name + " v.s. " + str(opp) )
        

    
    

    c_choice = c.c_select()

    p_choice = input ("Choose Rock, Paper, or Scissors ")
    while (p_choice.lower() != "rock") and (p_choice.lower() != "paper") and (p_choice.lower() != "scissors"):

        p_choice = input ("Choose Rock, Paper, or Scissors ")
    
    print ("You did " + p_choice)
    print (opp + " did " + c_choice)
    print()
    if (c_choice == p_choice):
        print ("You guys tied...next round...")
        set += 1
        game (p, c, 1, opp)
    else:
        if (p_choice == "rock" and c_choice == "scissors") or (p_choice == "paper" and c_choice == "rock") or (p_choice == "scissors" and c_choice == "paper"):
            
            print (f"You, {p.name}, won!!!!")
            print (opp + " lost.")
            p.win()
        else:
            print (opp + " won.")
            print (f"You, {p.name}, lost.")
            
            p.lose()
            
        print ()
        print ()
    




def stats (p):
    p.stats()



def legacy (p):
    p.legacy()



def career (p, c): 
    reset (p,c)
    while (p.tourney < 20) and (p.active == True):
        season (p,c)
        reset (p,c)
    if (p.tourney == 21):
        print ("Alright, you have played the max...20 tournaments")
        p.tourney == 20
    legacy (p)
    




print ("This is the career of one of the greatest Rock Paper Scissors players ever!!!!")






name = input ("Enter your name: ")
p = Player (name)


c = Computer ()

career (p,c)


    










