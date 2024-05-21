from policy import Policy
import numpy as np

class ValueIterationPolicy(Policy):
    def __init__(self, maze, gamma):
        super().__init__(maze)
        self.gamma = gamma
        self.values = None
        self.policy = self._value_iteration()
    
    def select_action(self, current_state):
        return self.p[current_state[0]][current_state[1]]

    def _value_iteration(self):
        delta = 1
        threshold = 0.01
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
                        temp.append(reward + self.gamma * old_values[state[0]][state[1]])
                        delta = max(delta, abs(old_values[state[0]][state[1]] - new_values[state[0]][state[1]]))
                    new_values[x, y] = max(temp)
                    
            old_values = new_values
        self.values = old_values
        self.p = self.policy(old_values)

    def policy(self, values):
        policy = np.empty((4, 4), dtype=object)
        for y, row in enumerate(values):
            for x, _ in enumerate(row):
                if [y,x] in self.maze.terminal_states:
                    policy[y, x] = 0
                    continue
                temp = []
                temp2 = []
                for state in self.get_possible_moves(y, x):
                    reward = self.maze.maze[state[0]][state[1]]
                    temp.append(reward + self.gamma * values[state[0]][state[1]])
                    temp2.append(state)
                policy[y, x] = temp2[np.argmax(temp)]
   
        return self.policy_to_directions(policy)
    

    def policy_to_directions(self, policy):
        directions = np.empty(policy.shape, dtype=object)
        for y, row in enumerate(policy):
            for x, move in enumerate(row):
                if move == 0:
                    directions[y, x] = None
                else:
                    dy, dx = move[0] - y, move[1] - x
                    if dy == -1:
                        directions[y, x] = 'up'
                    elif dy == 1:
                        directions[y, x] = 'down'
                    elif dx == -1:
                        directions[y, x] = 'left'
                    elif dx == 1:
                        directions[y, x] = 'right'
        return directions
    

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
        #refactor to step function:
        # out of bounds rules
        return moves
