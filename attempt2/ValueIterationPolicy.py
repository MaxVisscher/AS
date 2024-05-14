from policy import Policy
import numpy as np
import random

class ValueIterationPolicy(Policy):
    def __init__(self, maze):
        super().__init__(maze)
        self.values = None
        self.policy = self._value_iteration(maze.start_coordinates)

    def select_action(self, current_state):
        #@TODO:
        #Pick best possible mov
        pass
        

    def _value_iteration(self, start_state:list):
        delta = 1
        threshold = 0.01
        gamma = 0.9
        old_values =  np.zeros([4,4])
        while delta > threshold:
            new_values = old_values.copy()
            delta = 0
            for y, row in enumerate(self.maze.maze):
                for x, _ in enumerate(row):
                    if [y, x] in self.maze.terminal_states:
                        continue
                    temp = []
                    for state in self.get_possible_moves(x, y):
                        reward = self.maze.maze[state[0]][state[1]]
                        temp.append(reward + gamma * old_values[state[0]][state[1]])
                        delta = max(delta, abs(old_values[state[0]][state[1]] - new_values[state[0]][state[1]]))
                    new_values[x, y] = max(temp)
                    
            old_values = new_values
            print(old_values)
            
        print(new_values)
                    
    def get_possible_moves(self, y, x):
        moves = []
        if y > 0:
            moves.append((y-1, x))
        if y < len(self.maze.maze) - 1:
            moves.append((y+1, x))
        if x > 0:
            moves.append((y, x-1))
        if x < len(self.maze.maze[0]) - 1:
            moves.append((y, x+1))
        moves.append((y,x))
        return moves
