import random

computer = 0
human = 0


def main():
    # start execution
    print_instructions()
    computer_move(computer, human)


def print_instructions():
    # tell the user the rules of the game. What words you use is up to you.
    print("This prints the instruction of the game")


def computer_move(computer_score, human_score):
    # the computer rolls some number of times, displays the result of each roll, and the function returns the result
    # (0 or the total of the rolls). The function should use its parameters in order to play more intelligently (wish to
    # gamble more aggressively if it is behind)
    global computer
    global human
    print("computer score before rolling is " + str(computer))
    computer = computer + random.randint(1, 6)
    print("computer score after rolling is " + str(computer))
    human_move(computer, human)


def human_move(computer_score, human_score):
    show_current_status(computer_score, human_score)
    roll()
    print("the rolled number is " + str(rolled_number) + ". human score is now " + str(human_score))


def is_game_over(computer_score, human_score):
    # returns True if either player >=50, and the players are NOT tied. Otherwise returns False (Hint: call after
    # the human's move)
    print("calling is_game_over")


def roll():
    # returns random number 1-6, inclusive. randint method: https://docs.python.org/3/library/index.html
    print("starts to roll")
    while True:
        rolled_number = random.randint(1, 6)
        print("rolled number is " + str(rolled_number))
        global human
        human = human + rolled_number
        print("updated human score is " + str(human))
        ask_yes_or_no()


def ask_yes_or_no():
    # ask_yes_or_no(prompt)?
    # print user prompt like "Roll again?"
    prompt = input("roll again?")
    if prompt == "yes":
        return True
    else:
        show_current_status(computer, human)
        computer_move(computer, human)


def show_current_status(computer_score, human_score):
    # prints the user's current score and the computer's current score,
    # how far behind the user is, or if there is a tie.
    # call this before and after the human's move
    print("human score is now " + str(human) + ". computer score is now " + str(computer))
    if human - computer > 0:
        print("human is leading computer by " + str(human - computer))
    elif human - computer == 0:
        print("human and computer are tied")
    else:
        print("computer is leading human by " + str(computer - human))


def show_final_results(computer_score, human_score):
    # whether the human win or lost, and by how much (Hint: call this when the game has ended)
    print("calling show_final_results")


if __name__ == "__main__":
    main()
