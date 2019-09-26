import random

'''
Name: Xiexiao Luo
PennID: 70364612
Statement of work: I have completed this assignment alone without help
'''

'''Tower Blaster, a game that involves re-arranging a group of bricks in order to have an increasing sequence'''


# user vs. computer

# computer: reasonable strategy. human does not always beat computer

# objective: be the first player to arrange 10 bricks in your own tower from lowest to highest

# construct pile of 60 bricks, each numbers 1 to 60
# number is the width of the bricks

# human_tower = []
# computer_tower = []
#
#
# #shuffle the main pile at the start of each game
# print(main_pile.shuffle())
#
# #new bricks must be placed on top
# main_pile.pop()
# human_tower.push()
# computer_tower.push()

# after the first 10 bricksare dealt to user &10 dealt to computer -> 40 remaining in main_pile
# len(main_pile) == 40  #--> turn first card face down to discard

# each turn


# functions
def setup_bricks():
    '''construct pile of 60 bricks, each numbers 1 to 60.
        number is the width of the bricks'''

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
    random.shuffle(bricks)


def check_bricks(main_pile, discard):
    if main_pile == 0:
        piles_tuple[0] = shuffle_bricks(discard)
        piles_tuple[1].append(piles_tuple[0][0])


# TODO: what is this function for? where is it used?
def check_tower_blast(tower):
    # each element in the tower should be smaller than the next element
    for i in tower:
        # returns True if stability is achieved
        if tower[i] < tower[i + 1]:
            stability = True


def get_top_brick(brick_pile):
    # remove and return the first element of a list
    dealt_card = brick_pile.pop(0)
    return dealt_card


def deal_initial_bricks(main_pile):
    user_tower = []
    computer_tower = []

    # start dealing 10 cards(rounds)
    for i in range(1, 11):
        computer_tower.append(get_top_brick(main_pile))
        user_tower.append(get_top_brick(main_pile))

    # constructs a tuple containing computer hand and user hand
    global towers_tuple
    towers_tuple = (user_tower, computer_tower)

    return towers_tuple


def add_brick_to_discard(brick, discard):
    '''add the given brick to the top of the given discard pile'''
    discard.append(brick[0])


def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    # prompt user to choose a brick to be replaced

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
    discard.append(brick_to_be_replaced)

    return tower

    # tells user which brick is to be replaced by which brick
    print("You replaced", brick_to_be_replaced, "with ", new_brick)


def computer_play(tower, main_pile, discard):
    print("COMPUTER'S TURN")

    check_tower_blast(tower)
    pass


# TODO: move user play actions in main function here
def user_play():
    pass


def main():
    # calls setup_bricks to get a tuple of two lists.
    setup_bricks()

    # shuffle the bricks in the main pile
    shuffle_bricks(piles_tuple[0])

    # deal the first 10 cards to computer and user, respectively
    deal_initial_bricks(piles_tuple[0])

    print("printing piles tuple", piles_tuple)

    add_brick_to_discard(piles_tuple[0], piles_tuple[1])

    # TODO: start computer's turn'
    computer_play(towers_tuple[1], piles_tuple[0], piles_tuple[1])

    # start user's turn
    print("NOW IT'S YOUR TURN!")
    print("Your Tower: ", towers_tuple[0])
    print("The top brick on the discard pile is", piles_tuple[1][0])

    # TODO: 'H for help'
    which_pile = input("Type 'D' to take the discard brick, 'M' for a mysterious brick")
    if which_pile == "D":
        new_brick = piles_tuple[1][0]
        print("Your picked", new_brick, "from discard pile")
    else:
        new_brick = piles_tuple[0][0]
        print("Your picked", new_brick, "from main pile")

    # calling find_and_replace function
    # ask user input on where to put this brick
    brick_to_be_replaced = input("Where do you want to place this brick? Type a brick number to replace im your tower.")

    # check if the brick user inputs (brick_to_be_replaced) is acutaly the user's pile

    if int(brick_to_be_replaced) in towers_tuple[0]:
        find_and_replace(new_brick, brick_to_be_replaced, towers_tuple[0], piles_tuple[0])

    else:
        brick_to_be_replaced = input("please enter a number in your tower")

    print(towers_tuple[0])


if __name__ == "__main__":
    main()

# TODO: write unittest for each function if applicable
