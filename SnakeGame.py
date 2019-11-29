import numpy as np
import matplotlib.pyplot as plt

class SnakeGame:


    def __init__(self, size=6):
        self.grid = self.make_grid(size)
        self.grid_size = size
        self.move_snake_body = self.v_move_snake_body()
        self.plot_snake = self.v_plot_snake()
        self.dead = False
        self.head_val = 3

        self.spawn_reward()
        self.plot_grid()

    def plot_grid(self):
        plt.matshow(self.plot_snake(self.grid, self.head_val))
        plt.show()

    @staticmethod
    def v_plot_snake():
        def plot_snake(pixel, head_val):
            if pixel > 0 and not pixel == head_val:
                return 1
            elif pixel == head_val:
                return 2
            else:
                return pixel
        v_plot_snake = np.vectorize(plot_snake)
        return v_plot_snake

    @staticmethod
    def v_move_snake_body():
        def move_snake_body(segment):
            if segment > 0:
                return segment - 1
            else:
                return segment
        v_move_snake_body = np.vectorize(move_snake_body)
        return v_move_snake_body

    def move_snake(self, direction):
        if self.dead:
            print(f'You died, your score was {self.head_val-3}')
            return
        grid = self.grid
        head_val = self.head_val
        head_loc = self.find_head_loc(grid, head_val)
        new_head_loc = self.new_end_loc(head_loc, direction)
        self.dead = self.fatal_move(grid, new_head_loc)
        if not self.dead:
            self.grid = self.update_grid(grid, new_head_loc)
            self.plot_grid()
        else:
            self.plot_grid()
            print(f'You died, your score was {self.head_val-3}')
        return

    def update_grid(self, grid, head_loc):
        #reward?
        if grid[head_loc[0], head_loc[1]] == -2:
            self.head_val += 1
            self.spawn_reward()
        else:
            grid = self.move_snake_body(grid)
        grid[head_loc[0], head_loc[1]] = self.head_val
        return grid

    def spawn_reward(self):
        reward_spawned = False
        while not reward_spawned:
            spawn_loc = self.random_index(self.grid_size)
            if self.grid[spawn_loc[0], spawn_loc[1]] == 0 and not self.grid[spawn_loc[0], spawn_loc[1]] == -2:
                self.grid[spawn_loc[0], spawn_loc[1]] = -2
                reward_spawned = True

    @staticmethod
    def random_index(grid_size):
        return [np.random.randint(1, grid_size-1), np.random.randint(1, grid_size-1)]

    @staticmethod
    def fatal_move(grid, new_head_loc):
        return grid[new_head_loc[0], new_head_loc[1]] not in [0, -2]

    @staticmethod
    def new_end_loc(end_loc, direction):
        if direction == 'up':
            return end_loc + np.array([-1, 0])
        elif direction == 'down':
            return end_loc + np.array([1, 0])
        elif direction == 'left':
            return end_loc + np.array([0, -1])
        elif direction == 'right':
            return end_loc + np.array([0, 1])
        else:
            raise ValueError('Invalid direction')

    @staticmethod
    def find_head_loc(grid, head_val):
        # find head
        return np.array(np.where(grid == head_val)).flatten()



    @staticmethod
    def make_grid(size):
        """
        Makes a size x size array that represents the initial snake grid.
        """
        assert size > 4
        assert type(size) == int
        # initialise all to empty space
        game_board = np.reshape(np.zeros(size*size), (size, size))
        # fill in border
        game_board[0] = np.full(size, -1)
        game_board[size-1] = np.full(size, -1)
        for row_index in range(1, size-1):
            game_board[row_index][0] = -1
            game_board[row_index][size-1] = -1
        # add snake
        game_board[1][1] = 1
        game_board[1][2] = 2
        game_board[1][3] = 3
        return game_board
