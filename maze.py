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
        self.terminal_states = [[0,3], [3,0]]
        self.agent_pos = self.start_coordinates

    def step(self, state, action):

        copy_state = list(state)
        if action == "up":
            if state[0] > 0:
                copy_state[0] -= 1
        elif action == "down":
            if state[0] < len(self.maze) - 1:
                copy_state[0] += 1
        elif action == "left":
            if state[1] > 0:
                copy_state[1] -= 1
        elif action == "right":
            if state[1] < len(self.maze[0]) - 1:
                copy_state[1] += 1
        self.agent_pos = copy_state
        return tuple(copy_state)
    