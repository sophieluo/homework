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
    stability = True
    for i in range(0, len(tower)-1):

        # returns False if any of the numbers is greater than the number after it
        if tower[i] > tower[i + 1]:

            stability = False

    return stability


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

    # tells user which brick is to be replaced by which brick
    print("Replaced", brick_to_be_replaced, "with", new_brick)

    print("New tower is now", tower)
    print("###############")

    return tower


def computer_play(tower, main_pile, discard):
    print("###############")
    print("COMPUTER'S TURN")
    print("Computer's Tower:", tower)

    #replace the largest brick in the tower
    brick_to_be_replaced = max(tower)

    if discard[0] < 30:
        find_and_replace(discard[0], brick_to_be_replaced, towers_tuple[1], piles_tuple[0])
    else:
        find_and_replace(main_pile[0], brick_to_be_replaced, towers_tuple[1], piles_tuple[0])

    if check_tower_blast(tower) == True:
        print("Computer Wins!")
    else:
        user_play()


def user_play():
    # start user's turn
    print("###############")
    print("NOW IT'S YOUR TURN!")
    print("Your Tower: ", towers_tuple[0])
    print("The top brick on the discard pile is", piles_tuple[1][0])


    which_pile = input("Type 'D' to take the discard brick, 'M' for a mysterious brick")
    if which_pile == "D":
        new_brick = piles_tuple[1][0]
        print("Your picked", new_brick, "from discard pile")
    elif which_pile == "M":
        new_brick = piles_tuple[0][0]
        print("Your picked", new_brick, "from main pile")
    # TODO: 'H for help'
    elif which_pile == "H":
        print("do oyu need help")
    # TODO:repeat asking
    else:
        which_pile == input("Type 'D' to take the discard brick, 'M' for a mysterious brick")

    # calling find_and_replace function
    # ask user input on where to put this brick
    brick_to_be_replaced = input("Where do you want to place this brick? Type a brick number to replace in your tower.")

    # check if the brick user inputs (brick_to_be_replaced) is acutaly the user's pile

    if int(brick_to_be_replaced) in towers_tuple[0]:
        find_and_replace(new_brick, brick_to_be_replaced, towers_tuple[0], piles_tuple[0])
    else:
        brick_to_be_replaced = input("please enter a number in your tower")

    if check_tower_blast(towers_tuple[0]) == True:
        print("User Wins!")
    else:
        computer_play(towers_tuple[1], piles_tuple[0], piles_tuple[1])


def main():
    # calls setup_bricks to get a tuple of two lists.
    setup_bricks()

    # shuffle the bricks in the main pile
    shuffle_bricks(piles_tuple[0])

    # deal the first 10 cards to computer and user, respectively
    deal_initial_bricks(piles_tuple[0])

    # print("printing piles tuple", piles_tuple)

    #adds the first brick to the discard pile
    add_brick_to_discard(piles_tuple[0], piles_tuple[1])

    #removes the first brick from the main_pile
    get_top_brick(piles_tuple[0])

    #start computer's turn
    computer_play(towers_tuple[1], piles_tuple[0], piles_tuple[1])



if __name__ == "__main__":
    main()

# TODO: write unittest for each function if applicable
