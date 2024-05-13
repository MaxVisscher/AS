import numpy as np

class Maze:
    def __init__(self):
        self.maze = np.array([
                            [-1, -1, -1, 40],
                            [-1, -1, -10, -10],
                            [-1, -1, -1, -1],
                            [10, -2, -1, -1]
                        ])
        self.start_coordinates = [3,2]
        self.current_pos = self.start_coordinates
        