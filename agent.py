class Agent:
    def __init__(self, maze, policy, start_coordinates):
        self.maze = maze
        self.policy = policy
        self.current_state = start_coordinates
        self.visited = []
        self.reward = 0
        self.expected_value = 0

    def value(self, state):
        self.reward += self.maze.maze[state[0], state[1]]


    def act(self):
        self.current_state = self.maze.step(
            self.current_state, 
            self.policy.select_action(self.current_state)
        )
        self.value(self.current_state)
