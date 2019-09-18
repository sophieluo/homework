import random

current_computer_score = 0
current_human_score = 0
total_human_score_this_turn = 0


def main():
    # start execution
    print_instructions()
    computer_move(current_computer_score, current_human_score)


def print_instructions():
    # tell the user the rules of the game. What words you use is up to you.
    print("This prints the instruction of the game")


def computer_move(computer_score, human_score):
    # the computer rolls some number of times, displays the result of each roll, and the function returns the result
    # (0 or the total of the rolls). The function should use its parameters in order to play more intelligently (wish to
    # gamble more aggressively if it is behind)
    global current_computer_score
    global current_human_score
    print("computer starts to roll")
    print("computer score before rolling is " + str(current_computer_score))
    computer_rolled_number = random.randint(1, 6)
    if computer_rolled_number == 6:
        computer_rolled_number = 0
    current_computer_score = current_computer_score + computer_rolled_number
    print("computer score after rolling is " + str(current_computer_score))
    human_move(current_computer_score, current_human_score)


def human_move(computer_score, human_score):
    show_current_status(computer_score, human_score)
    global total_human_score_this_turn
    total_human_score_this_turn = 0
    roll()


def is_game_over(computer_score, human_score):
    # returns True if either player >=50, and the players are NOT tied. Otherwise returns False (Hint: call after
    # the human's move)
    print("calling is_game_over")
    if current_computer_score >= 50 or current_human_score >= 50:
        print("game is over. checking results")
        show_final_results(current_computer_score, current_human_score)
        # return True
    else:
        ask_yes_or_no()
        # computer_move(computer, human)


def roll():
    # returns random number 1-6, inclusive. randint method: https://docs.python.org/3/library/index.html
    print("human starts to roll")
    while True:
        global current_human_score
        rolled_number = random.randint(1, 6)
        print("rolled number is " + str(rolled_number))
        if rolled_number != 6:
            current_human_score = current_human_score + rolled_number
            global total_human_score_this_turn
            total_human_score_this_turn = total_human_score_this_turn + rolled_number
            print("updated human score is " + str(current_human_score))
            is_game_over(current_computer_score, current_human_score)
        else:
            print("oops, rolled a 6")
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