from maze import Maze
from policy import Policy

class Agent:
    def __init__(
            self, 
            maze : Maze, 
            policy: Policy, 
            start_coordinates
        ):
        self.maze = maze
        self.policy = policy
        self.current_state = start_coordinates
        self.visited = []
        self.reward = 0
        self.expected_value = 0

    def value(self, state):
        self.reward += self.maze.maze[state[0], state[1]]


    def act(self):
        self.maze.step(
            self.maze.agent_pos, 
            self.policy.select_action(self.maze.agent_pos)
        )
            
        self.value(self.maze.agent_pos)