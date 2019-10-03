'''
Name: Xiexiao Luo
PennID: 70364612
Statement of work: I have completed this assignment alone without help
List of inputs that leads to a "win": [0,0,0,0,0,0,0,0,0,0,50,30]
List of inputs that lead to a "loss":[0,0,0,0,0,0,0,0,0,0,0]
'''

def main ():
    """performs the main functions of the lunar landing program.
    asks users to input how much fuel to burn in each round, calculates the velocity and altitude
    """
    altitude = 100
    fuel = 100
    velocity = 0
    while altitude > 0:
    # print("start here")
    # normalizes fuel_burnt
        fuel_burnt = input("How much fuel you want to burn?")
    #     print(type(fuel_burnt))
        try:
            fuel_burnt = int(fuel_burnt)
            if fuel_burnt <= 0:
                fuel_burnt = 0
            elif fuel_burnt > fuel:
                fuel_burnt = fuel
            elif fuel <= 0:
                alert ("Ran out of fuel.")
                fuel_burnt = 0
            else:
                fuel_burnt = fuel_burnt
            velocity = velocity + 1.6 - fuel_burnt * 0.15
            print("your velocity is " + str(velocity))
    # calculates fuel level at end of this round
            fuel -= fuel_burnt
            print("your fuel level is " + str(fuel))
    # calculates altitude at end of this round
            altitude -= velocity
            print("your altitude is " + str(altitude))
        except ValueError:
            print("That's not an integer! Please enter an integer")
    # checks if laning velocity is greater than 10
    if velocity <= 10:
        print ("You landed safely! Your altitude is " + str(altitude) + ". Your landing velocity was " + str(velocity))
    else:
        print ("Ooops! Crashed! Your landing velocity was " + str(velocity) + ".")
    play_again()

# asks if user wants to play again
def play_again ():
    is_again = input("Do you want to play again?")
    if is_again[0] == "y" or is_again[0] == "Y":
        print(is_again[0])
        print("Great! Let's try one more time!")
        main_function()
    elif is_again[0] == "n" or is_again[0] == "N":
        print ("See you next time!")
    else:
        play_again()

# help(main())
# calls the main to start playing
if __name__ == "__main__":
    main()
