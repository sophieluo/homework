import unittest

from tower_blaster import *


class TestTowerBlaster(unittest.TestCase):

    def test_check_tower_blast(self):

        tower_blast = check_tower_blast([1, 2, 3])

        self.assertEqual(tower_blast, True)

    def test_get_top_brick(self):

        first_card = get_top_brick([1, 3, 5])

        self.assertEqual(first_card, 1)

    def test_deal_initial_bricks(self):

        test_towers_tuple = deal_initial_bricks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

        self.assertEqual(test_towers_tuple, ([20, 18, 16, 14, 12, 10, 8, 6, 4, 2], [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]))

    def test_add_brick_to_discard(self):

        # discard = [1, 2, 3]
        # brick = 0

        self.assertEqual(add_brick_to_discard(0, [1, 2, 3]), [0, 1, 2, 3])

    def test_find_and_replace(self):

        new_brick = 1
        brick_to_be_replaced = 2
        tower = [2, 3, 4]
        discard = []

        self.assertEqual(find_and_replace(new_brick, brick_to_be_replaced, tower, discard), True)

    def test_computer_play(self):

        pass

    def test_user_play(self):

        pass


if __name__ == '__main__':
    unittest.main()
