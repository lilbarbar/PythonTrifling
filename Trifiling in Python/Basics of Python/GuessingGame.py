name = input ("Enter your name: ")
number = 8
num_of_guesses = 1
guess = input("Guess the hidden number between 1 and 20 ")
while (int(guess) != int(number) ) and (num_of_guesses <= 5):
    print ("Incorrect, guess again...")
    num_of_guesses += 1
    guess = input("Guess the hidden number between 1 and 20 ")

if int(guess) == int(number):
    print (f"Yes you got it, {name}!")
else:
    print (f"You did not get it, {name}. The number was " + str(number) )

