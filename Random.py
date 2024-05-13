from Agent import Agent
import random
class Random(Agent):
    def __init__(self, maze, start_coordinates):
        super().__init__(maze, start_coordinates)

    def pick_move(self):
        possible_moves = ["up", "down", "left", "right"]
        return random.choice(possible_moves)