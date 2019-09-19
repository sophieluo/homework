import random

current_computer_score = 0
current_human_score = 0
total_human_score_this_turn = 0


def main():
    # start execution
    """the main() function is where the program starts execution.
    The lines at the bottom t runs the main function"""

    # calls the function print_instructions, which prints out the instructions for this game
    print_instructions()

    # calls the function computer_move and passes current_computer_score and current_human_score into it
    computer_move(current_computer_score, current_human_score)


def print_instructions():
    """this function prints out the instruction of the game.
    tells users the rules of the game and what the user is expected to enter"""

    # stores instructions in a variable called instruction, then prints out the instructions
    instruction = "Pig is a very simple game. Two players take turns; on each turn, a player rolls a six-sided die as " \
                  "many times as she wishes, or until she rolls a 6. Each number she rolls, except a 6, is added to " \
                  "her score this turn; but if she rolls a 6, her score for this turn is zero, and her turn ends. At " \
                  "the end of each turn, the score for that turn is added to the player's total score. The first " \
                  "player to reach or exceed 50 wins. "
    print(instruction)


def computer_move(computer_score, human_score):
    """this function emulates a computer move. For simplicity, here the computer rolls only once in each turn.
    It does not take strategic decisions based on the current status.
    """

    # make the two variables global variables
    global current_computer_score
    global current_human_score

    # prints out the computer score before this roll
    print("computer starts to roll")
    print("computer score before rolling is " + str(current_computer_score))

    # computer rolls a random number between 1 and 6, inclusive
    computer_rolled_number = random.randint(1, 6)

    # if computer rolls a 6, set it to 0 (according to the rules)
    if computer_rolled_number == 6:
        computer_rolled_number = 0

    # calculates computer score after this roll
    current_computer_score = current_computer_score + computer_rolled_number

    # displays computer score after this roll
    print("computer score after rolling is " + str(current_computer_score))

    # calls human_move function. now it's the human's turn!
    human_move(current_computer_score, current_human_score)


def human_move(computer_score, human_score):
    """ this function emulates a human's turn, which may include a single roll or multiple rolls.
    The player can choose to roll once or multiple times. the final result equal rolled number in each roll added up,
    and is stored in a variable called total_human_score_this_turn. However, if the human rolls a 6, he has to stop,
    and the total_human_score_this_turn is set to 0
    """

    # checks the current status (who is leading and by how much) before human starts to roll
    show_current_status(computer_score, human_score)

    # set the total_human_score_this_turn to be a global variable and set it to 0
    global total_human_score_this_turn
    total_human_score_this_turn = 0

    # human starts to roll. For each turn, human has to roll at least once,
    # so no need to ask before rolling for the first time
    roll()


def is_game_over(computer_score, human_score):
    """ this function checks if either either gets to >= 50.
    it returns True if either player <=50, and the players ar NOT tied"""

    print("calling is_game_over")

    # TODO: should return True if >=50 and not tied

    # checks if either player >= 50
    if current_computer_score >= 50 or current_human_score >= 50:
        print("game is over. checking results")
        show_final_results(current_computer_score, current_human_score)
        # return True

    # both players are not 50 yet, asks human whether to roll again
    else:
        ask_yes_or_no()


def roll():
    """ this function returns a random number 1-6, inclusive"""

    print("human starts to roll")
    while True:
        global current_human_score

        # rolls a random number from 1-6, inclusive and stores it in a variable called rolled_number
        rolled_number = random.randint(1, 6)

        # prints out the rolled number
        print("rolled number is " + str(rolled_number))

        # checks if rolled number is 6.
        # if it's not 6, increment current_human_score by the rolled number. then calculate total_human_score_this_turn
        # if it is 6, set current_human_score to 0. the human ends this turn with 0
        if rolled_number != 6:
            current_human_score += rolled_number

            # calculates human's score for this turn (one turn is one or multiple draws)
            global total_human_score_this_turn
            total_human_score_this_turn += rolled_number

            # prints out the updated human score after this roll (not this turn)
            print("updated human score is " + str(current_human_score))

            # checks if any of current_human_score or current_computer_score gets greater than 50
            # checks this only after human rolls because computer rolls first. humans should get one more turn
            is_game_over(current_computer_score, current_human_score)

        # if the rolled number is 6
        else:
            print("oops, rolled a 6")

            # revert current_human_score to its value at the end of last turn by subtracting current_human_score
            # by the number human cumulative during this turn
            current_human_score = current_human_score - total_human_score_this_turn


def ask_yes_or_no():
    # ask_yes_or_no(prompt)?
    # print user prompt like "Roll again?"
    prompt = input("roll again?")
    if prompt[0] == "y" or prompt[0] == "Y":
        return True
    elif prompt[0] == "n" or prompt[0] == "N":
        show_current_status(current_computer_score, current_human_score)
        computer_move(current_computer_score, current_human_score)
    else:
        ask_yes_or_no()


def show_current_status(computer_score, human_score):
    # prints the user's current score and the computer's current score,
    # how far behind the user is, or if there is a tie.
    # call this before and after the human's move
    print("human score is now " + str(current_human_score) + ". computer score is now " + str(current_computer_score))
    if current_human_score - current_computer_score > 0:
        print("human is leading computer by " + str(current_human_score - current_computer_score))
    elif current_human_score - current_computer_score == 0:
        print("human and computer are tied")
    else:
        print("computer is leading human by " + str(current_computer_score - current_human_score))


def show_final_results(computer_score, human_score):
    # whether the human win or lost, and by how much (Hint: call this when the game has ended)
    print("calling show_final_results")
    if current_computer_score > current_human_score:
        print("computer wins!")
    elif current_computer_score < current_human_score:
        print("human wins!")
    else:
        print("computer and human are tied!")


if __name__ == "__main__":
    main()