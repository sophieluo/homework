import unittest

from tower_blaster import *


class TestTowerBlaster(unittest.TestCase):
    def test_setup_bricks(self):
        self.assertEqual(True, False)

    def test_get_top_brick(self):
        self.assertEqual(setup_bricks("[1, 2, 3]"), 1)


if __name__ == '__main__':
    unittest.main()
