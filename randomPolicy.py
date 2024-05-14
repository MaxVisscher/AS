from policy import Policy
import random

class RandomPolicy(Policy):
    def __init__(self):
        super().__init__()

    def select_action(self,state = None, maze = None):
        possible_actions = ["up", "down", "left", "right"]
        return random.choice(possible_actions)
    