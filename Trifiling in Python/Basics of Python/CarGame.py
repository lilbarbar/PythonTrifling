instructions = '''
Driving Game
Type Start to start the car if it is off
Type Drive to Drive the car
Type Stop to stop the car
Type Quit to exit the car
'''

print (instructions)


action = input ("What do you wanna do: ")

in_car = True
car_on = False

while in_car == True:
    if action.upper() == "HELP":
        print (instructions)
    if action.upper() == "START":
        if not car_on:
            print ("Starting the car... DING! The Car is now on!")
            car_on = True
        else:
            print ("The car is already on.")
    elif action.upper() == "DRIVE":
        if car_on:
            print ("VROOOM! YOU ARE CRUISING")
        else:
            print ("Car is off...start the car to drive!")
    elif action.upper() == "STOP":
        if car_on:
            print ("You stopped the car")
            car_on = False
        else:
            print ("Car is off...you cannot stop a car that is already stopped")
    elif action.upper() == "QUIT":
        if not car_on:
            print ("You exited the car!")
            in_car = False
        else:
            print ("Car must be off for the car to be stopped!")
    elif action.upper() == "HELP":
        print (instructions)
    else:
        print ("I have no idea what you are trying to say...")

    if ( (action.upper() != "QUIT" )or  (action.upper() == "QUIT" and car_on)):
        action = input ("What do you wanna do: ")
    
        

print ("Thanks for playing!")
