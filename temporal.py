from agent import Agent
from policy import Policy
import numpy as np

class TemporalDiff(Agent):
    def __init__(self, policy, episodes, gamma, maze, start_coordinates):
        super().__init__(maze, policy, start_coordinates)
        self.OptimalPolicy = policy
        self.gamma = gamma
        
        # for each in self.episodes:
        #     print(each)
            

    # def _generate_episodes(self):
    #     episodes = []
    #     for x in range(len(self.OptimalPolicy)):
    #         for y in range(len(self.OptimalPolicy[0])):
    #             if self.OptimalPolicy[x][y] != None:
    #                 episodes.append(
    #                     self._get_episode(
    #                         self.OptimalPolicy, 
    #                         x, 
    #                         y
    #                     )
    #                 )
    #     return episodes

    # def _get_state(self, policy, x, y):
    #     episode = []
    #     while policy[x][y] != None:
    #         episode.append(policy[x][y])
    #         if policy[x][y] == 'up':
    #             x -= 1
    #         elif policy[x][y] == 'down':
    #             x += 1
    #         elif policy[x][y] == 'left':
    #             y -= 1
    #         elif policy[x][y] == 'right':
    #             y += 1

    #     return ((x,y), episode)

    def temporal_difference(self, episodes, policy, start, step_size):
        values = np.zeros((4, 4))
        for _ in range(episodes):
            state = start
            while state not in self.maze.terminal_states:
                x, y = state
                action = policy[x][y]
                next_state = self.maze.step(state, action)
                values[state[0]][state[1]] += step_size * (
                    self.maze.maze[next_state[0]][next_state[1]] + \
                    self.gamma * values[next_state[0]][next_state[1]] - \
                    values[state[0]][state[1]]
                )
                state = next_state
        print(values)

