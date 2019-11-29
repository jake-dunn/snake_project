import unittest
import numpy as np
from SnakeGame import SnakeGame


class TestSnakeGame(unittest.TestCase):

    def test_make_grid_input(self):
        sg = SnakeGame(test=True)
        # input must be an int
        self.assertRaises(Exception, sg.make_grid, 6.3)
        self.assertRaises(Exception, sg.make_grid, 'Snake')
        # input must be 5 or greater
        self.assertRaises(Exception, sg.make_grid, 2)

    def test_make_grid(self):
        # 6 -> [[-1,-1,-1,-1,-1,-1],
        #       [-1, 1, 2, 3, 0,-1],
        #       [-1, 0, 0 ,0, 0, 4],
        #       [-1, 0, 0, 0, 0,-1],
        #       [-1, 0, 0, 0, 0,-1],
        #       [-1,-1,-1,-1,-1,-1]]
        sg = SnakeGame()
        expected_grid = np.array([[-1, -1, -1, -1, -1, -1], [-1, 1, 2, 3, 0, -1], [-1, 0, 0, 0, 0, -1],
                                  [-1, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, -1], [-1, -1, -1, -1, -1, -1]])
        np.testing.assert_equal(sg.make_grid(6), expected_grid)

    def test_find_head_loc(self):
        # find location of snake head
        #      [[-1,-1,-1,-1,-1,-1],
        #       [-1, 1, 2, 3, 0,-1],
        #       [-1, 0, 0 ,0, 0, 4],
        #       [-1, 0, 0, 0, 0,-1],
        #       [-1, 0, 0, 0, 0,-1],
        #       [-1,-1,-1,-1,-1,-1]]
        # -> (1,3)
        sg = SnakeGame(test=True)
        head_loc = sg.find_head_loc(sg.grid, 3)
        np.testing.assert_equal(head_loc, np.array([1, 3]))

    def test_new_end_loc(self):
        sg = SnakeGame(test=True)
        head_loc = np.array([1, 3])
        np.testing.assert_equal(sg.new_end_loc(head_loc, 'down'), np.array([2, 3]))
        np.testing.assert_equal(sg.new_end_loc(head_loc, 'up'), np.array([0, 3]))
        np.testing.assert_equal(sg.new_end_loc(head_loc, 'left'), np.array([1, 2]))
        np.testing.assert_equal(sg.new_end_loc(head_loc, 'right'), np.array([1, 4]))
        self.assertRaises(ValueError, sg.new_end_loc, head_loc, 'error')

    def test_fatal_move(self):
        #      [[-1,-1,-1,-1,-1,-1],
        #       [-1, 1, 2, 3, 0,-1],
        #       [-1, 0, 0 ,0, 0, 4],
        #       [-1, 0, 0, 0, 0,-1],
        #       [-1, 0, 0, 0, 0,-1],
        #       [-1,-1,-1,-1,-1,-1]]
        # up and left -> True, down and right -> False
        sg = SnakeGame(test=True)
        grid = sg.grid
        head_loc_down = np.array([2, 3])
        head_loc_right = np.array([1, 4])
        head_loc_up = np.array([0, 3])
        head_loc_left = np.array([1, 2])
        self.assertEqual(sg.fatal_move(grid, head_loc_down), False)
        self.assertEqual(sg.fatal_move(grid, head_loc_right), False)
        self.assertEqual(sg.fatal_move(grid, head_loc_up), True)
        self.assertEqual(sg.fatal_move(grid, head_loc_left), True)

    def test_update_grid(self):
        # grid= [[-1,-1,-1,-1,-1,-1],
        #        [-1, 1, 2, 3, 0,-1],
        #        [-1, 0, 0 ,0, 0, 4],
        #        [-1, 0, 0, 0, 0,-1],
        #        [-1, 0, 0, 0, 0,-1],
        #        [-1,-1,-1,-1,-1,-1]]
        #   and new_head_loc np.array([2, 3]) ->
        #        [[-1,-1,-1,-1,-1,-1],
        #         [-1, 0, 1, 2, 0,-1],
        #         [-1, 0, 0 ,3, 0, 4],
        #         [-1, 0, 0, 0, 0,-1],
        #         [-1, 0, 0, 0, 0,-1],
        #         [-1,-1,-1,-1,-1,-1]]
        sg = SnakeGame(test=True)
        grid = sg.grid
        head_loc_down = np.array([2, 3])
        expected_updated_grid = np.array(
            [[-1, -1, -1, -1, -1, -1], [-1, 0, 1, 2, 0, -1], [-1, 0, 0, 3, 0, -1], [-1, 0, 0, 0, 0, -1],
             [-1, 0, 0, 0, 0, -1],
             [-1, -1, -1, -1, -1, -1]])
        np.testing.assert_equal(sg.update_grid(grid, head_loc_down), expected_updated_grid)
