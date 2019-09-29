import random

'''
Name: Xiexiao Luo
PennID: 70364612
Statement of work: I have completed this assignment alone without help
'''

'''Tower Blaster, a game that involves re-arranging a group of bricks in order to have an increasing sequence'''


# TODO: not sure why discard pile does not get updated after each round


# functions
def setup_bricks():
    """construct pile of 60 bricks, each numbers 1 to 60.
        number is the width of the bricks"""

    # creates main_pile and discard_piles and initialize them as empty lists
    main_pile_list = []
    discard_pile_list = []

    # put cards numbered 1-60 in main_pile
    for i in range(1, 61):
        main_pile_list.append(i)

    # create a tuple for the two piles of cards
    global piles_tuple
    piles_tuple = [main_pile_list, discard_pile_list]

    # returns the tuple
    return piles_tuple


def shuffle_bricks(bricks):
    """this function shuffles the given bricks"""

    random.shuffle(bricks)


# todo: need to call this every time user/computer starts to replace cards
def check_bricks(main_pile, discard):
    """checks if there's any cards left in the given main pile of bricks.
    If not, shuffle the discard pile and move those bricks to the main pile.
    Then turn over the top card to be the start of the new discard pile.
    """

    if main_pile == 0:
        piles_tuple[0] = shuffle_bricks(discard)
        piles_tuple[1].append(piles_tuple[0][0])


def check_tower_blast(tower):
    """checks if stability is achieved"""

    # each element in the tower should be smaller than the next element
    stability = True
    for i in range(0, len(tower) - 1):

        # returns False if any of the numbers is greater than the number after it
        if tower[i] > tower[i + 1]:
            stability = False

    return stability


# todo: this is also used during each player's turn. check to make sure
def get_top_brick(brick_pile):
    """Remove and return the top brick from any given pile of bricks.
    It is used at the start of game play for dealing bricks and during each player’s turn to take the top brick from
    either the discarded brick pile or from the main pile.
    This function returns an integer (number on the brick).
    """

    # remove and return the first element of a list
    dealt_card = brick_pile.pop(0)
    return dealt_card


def deal_initial_bricks(main_pile):
    """given a main_pile, deals 1 card to computer, 1 cards to user, then 1 card to computer, until computer and user
    both have 10 cards.

    computer receives cards first, and plays first.

    This function returns a tuple containing two lists -
    one representing the user’s hand and the other representing the computer’s hand.
    """

    user_tower = []
    computer_tower = []

    # start dealing 10 cards(rounds)
    for i in range(1, 11):
        computer_tower.insert(0, get_top_brick(main_pile))
        user_tower.insert(0, get_top_brick(main_pile))

    # constructs a tuple containing computer hand and user hand
    global towers_tuple
    towers_tuple = (user_tower, computer_tower)

    return towers_tuple


def add_brick_to_discard(brick, discard):
    """add the given brick to the top of the given discard pile"""

    discard.insert(0, brick)

    return discard


def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    """Find the given brick to be replaced in the given tower and replace it with the given new brick.
    Check and make sure that the given brick to be replaced is truly a brick in the given tower.
    The given brick to be replaced then gets put on top of the given discard pile.
    Return True if the given brick is replaced, otherwise return False.
    """

    # global index
    index = 0

    # find the index of the brick to be replaced
    for i in range(0, len(tower)):
        # cast brick_to_be_replaced to int, then see if it's equal to any element in the tower
        if tower[i] == int(brick_to_be_replaced):
            index = i

    # takes the brick to be replaced out of the pile
    tower.pop(index)

    # inserts the new brick into the pile at the desired location
    tower.insert(index, new_brick)

    # puts the brick to be replaced onto the top of the discard pile
    add_brick_to_discard(brick_to_be_replaced, discard)

    # tells user which brick is to be replaced by which brick
    print("Replaced", brick_to_be_replaced, "with", new_brick)

    print("New tower is now", tower)
    print("###############")

    # check if the given brick is replaced
    if tower[index] == new_brick and discard[0] == brick_to_be_replaced:
        return True



def computer_play(tower, main_pile, discard):
    """computer's turn
    computer plays according to given strategy
    checks if stability has been achieved after computer replaced the card
    """

    # todo: computer needs a better strategy
    print("###############")
    print("COMPUTER'S TURN")
    print("Computer's Tower:", tower)

    # replace the largest brick in the tower
    brick_to_be_replaced = max(tower)

    if discard[0] < 30:
        find_and_replace(discard[0], brick_to_be_replaced, towers_tuple[1], piles_tuple[1])

        # remove brick to be replaced from discard pile. one new card has been added to the top of the discard file,
        # so index changes to 1
        piles_tuple[1].pop(1)
    else:
        find_and_replace(main_pile[0], brick_to_be_replaced, towers_tuple[1], piles_tuple[1])
        # remove brick to be replaced from main pile. no new card has been added to the main pile, so index is still 0
        piles_tuple[0].pop(0)

    if check_tower_blast(tower) == True:
        print("Computer Wins!")
    else:
        user_play(towers_tuple[0], main_pile, discard)


def user_play(tower, main_pile, discard):
    """prompts user to choose which pile to get card from.
    then prompts user to choose which card to be replaced.
    checks if stability has been achieved after user replaced designated card
    """

    # start user's turn
    print("###############")
    print("NOW IT'S YOUR TURN!")
    print("Your Tower: ", tower)
    print("The top brick on the discard pile is", discard[0])

    # todo: should pop brick from respective file after inserting

    which_pile = input("Type 'D' to take the discard brick, 'M' for a mysterious brick")
    if which_pile == "D":
        new_brick = discard[0]
        print("Your picked", new_brick, "from discard pile")
        
    elif which_pile == "M":
        new_brick = main_pile[0]
        print("Your picked", new_brick, "from main pile")
    # TODO: 'H for help'
    elif which_pile == "H":
        print("do you need help")
    # TODO:repeat asking
    else:
        var = which_pile == input("Type 'D' to take the discard brick, 'M' for a mysterious brick")

    # todo: if chooses a card from the main_pile, can reject and put it in discard

    # calling find_and_replace function
    # ask user input on where to put this brick
    brick_to_be_replaced = int(input("Where do you want to place this brick? Type a brick number to replace in your tower."))

    # check if the brick user inputs (brick_to_be_replaced) is actually the user's pile

    if brick_to_be_replaced in tower:
        find_and_replace(new_brick, brick_to_be_replaced, tower, main_pile)
    else:
        brick_to_be_replaced = input("please enter a number in your tower")

    #checks if stability is achieved
    if check_tower_blast(tower) == True:
        print("User Wins!")
    else:
        computer_play(towers_tuple[1], main_pile, discard)


def main():
    """called at the start of the game. Sets up the game board, and start computer's first turn
    """

    # calls setup_bricks to get a tuple of two lists.
    setup_bricks()

    # shuffle the bricks in the main pile
    shuffle_bricks(piles_tuple[0])

    # deal the first 10 cards to computer and user, respectively
    deal_initial_bricks(piles_tuple[0])

    # adds the first brick to the discard pileå
    add_brick_to_discard(piles_tuple[0][0], piles_tuple[1])

    # removes the first brick from the main_pile
    get_top_brick(piles_tuple[0])

    # start computer's turn
    computer_play(towers_tuple[1], piles_tuple[0], piles_tuple[1])


if __name__ == "__main__":
    main()

