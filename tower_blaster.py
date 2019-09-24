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
main_pile = []
human_tower = []
computer_tower = []
for i in range (1, 61):
    main_pile.append(i)

# TODO: how to shuffle a list
print(main_pile.shuffle())

def start_game():
    main_pile.shuffle()
    return main_pile





def main():
    pass




if __name__ == "__main__":
    main()