class Agent:
    def __init__(self, maze, start_coordinates):
        self.maze = maze
        self.current_pos = start_coordinates
        self.visited = []
        self.moves = 0
        self.reward = 0
        self.done = False
        self.terminal_state = False


    def step(self, direction):
        if direction == "up":
            if self.current_pos[0] > 0:
                self.current_pos[0] -= 1
        elif direction == "down":
            if self.current_pos[0] < len(self.maze) - 1:
                self.current_pos[0] += 1
        elif direction == "left":
            if self.current_pos[1] > 0:
                self.current_pos[1] -= 1
        elif direction == "right":
            if self.current_pos[1] < len(self.maze[0]) - 1:
                self.current_pos[1] += 1
        print(self.current_pos)
        self.visited.append(list(self.current_pos))
        self.moves += 1
        self.reward += self.maze[self.current_pos[0]][self.current_pos[1]]
        if self.current_pos == [3, 0] or self.current_pos == [0, 3]:
            self.done = True
        return self.done

    def reset(self):
        self.current_pos = [0, 0]
        self.visited = []
        self.moves = 0
        self.reward = 0
        self.done = False
        return self.current_pos, self.reward, self.done
    
    def is_terminal(self):
    # i forgor if terminal means dead and fucked in an infinite loop or finished
    # gonna assume the first, but gonna factcheck before implementing
    # DO THIS IN THE SEMINAR WHOPOAAAA
        return self.terminal_state
    
    def pick_move(self):
        pass