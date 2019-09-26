import random

'''
Name: Xiexiao Luo
PennID: 70364612
Statement of work: I have completed this assignment alone without help
'''

'''Tower Blaster, a game that involves re-arranging a group of bricks in order to have an increasing sequence'''

# user vs. computer

# computer: reasonable strategy. human does not always beat computer

# must use lists and tuples
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

#after the first 10 bricksare dealt to user &10 dealt to computer -> 40 remaining in main_pile
# len(main_pile) == 40  #--> turn first card face down to discard

#each turn


#functions
def setup_bricks():
    #creates main_pile and discard_piles and initialize them as empty lists
    main_pile_list = []
    discard_pile_list = []

    #put cards numbered 1-60 in main_pile
    for i in range(1, 61):
        main_pile_list.append(i)

    #create a tuple for the two piles of cards
    global piles_tuple
    piles_tuple = (main_pile_list, discard_pile_list)


    #returns the tuple
    return piles_tuple


def shuffle_bricks(bricks):
    random.shuffle(bricks)


def check_bricks(main_pile, discard):
    if main_pile == 0:
        piles_tuple[0] = shuffle_bricks(discard)
        piles_tuple[1].append(piles_tuple[0][0])


def check_tower_blast(tower):
    #each element in the tower should be smaller than the next element
    for i in tower:
        #returns True if stability is achieved
        if tower[i] < tower[i+1]:
            stability = True


def get_top_brick(brick_pile):
    #remove and return the first element of a list
    dealt_card = brick_pile.pop(0)
    return dealt_card


def deal_initial_bricks(main_pile):
    user_pile_list = []
    computer_pile_list = []

    #start dealing 10 cards(rounds)
    for i in range(1, 11):
        computer_pile_list.append(get_top_brick(main_pile))
        user_pile_list.append(get_top_brick(main_pile))

    #constructs a tuple containing computer hand and user hand
    global hands_tuple
    hands_tuple = (user_pile_list, computer_pile_list)

    print(hands_tuple)
    return hands_tuple


def add_brick_to_discard(brick, discard):
    '''add the given brick to the top of the given discard pile'''
    discard.append(brick[0])


def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    pass


def computer_play(tower, main_pile, discard):
    print("COMPUTER'S TURN")
    pass






def main():
    #calls setup_bricks to get a tuple of two lists.
    setup_bricks()

    #shuffle the bricks in the main pile
    shuffle_bricks(piles_tuple[0])

    #deal the first 10 cards to computer and user, respectively
    deal_initial_bricks(piles_tuple[0])


if __name__ == "__main__":
    main()