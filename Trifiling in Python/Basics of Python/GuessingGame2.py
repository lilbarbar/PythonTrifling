number = 8
guess = int( input ("Enter a # between 1 and 10 "))
num_guesses = 0
won = False
num_guesses += 1
while (num_guesses < 3):
    if (guess == number):
        print ("You won!")
        won = True
        break
    else:
        print ("Wrong! New guess: ")
        guess = int( input ("Enter a # between 1 and 10 "))
    num_guesses += 1


if won:
    print ("Congrats!")
else:
    print ("You didn't win unfortunately, the # was 8.")

