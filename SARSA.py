import pygame
import numpy as np
import random
from agent import Agent

class Sarsa(Agent):
    def __init__(self, maze, policy, start_coordinates):
        super().__init__(maze, policy, start_coordinates)

    def sarsa(
            self, 
            epochs, 
            step_size, 
            gamma, 
            epsilon, 
            start_coordinates
        ):
        Qfunction = {}

        for _ in range(epochs):
            state = tuple(start_coordinates)
            if state not in list(Qfunction.keys()):
                Qfunction[state] = {
                    "up": 0,
                    "down": 0,
                    "left": 0,
                    "right": 0
                }

            action = max(Qfunction[state], key=Qfunction[state].get)
            if random.random() < epsilon:
                action = np.random.choice(
                    [
                        "up", 
                        "down", 
                        "left", 
                        "right"
                    ]
                )
            while list(state) not in self.maze.terminal_states:
                next_state = self.maze.step(state, action)
                reward = self.maze.maze[next_state[0]][next_state[1]]
                
                if next_state not in list(Qfunction.keys()):
                    Qfunction[next_state] = {
                        "up": 0, 
                        "down": 0,
                        "left": 0,
                        "right": 0
                    }
                next_action = max(
                    Qfunction[next_state], 
                    key=Qfunction[next_state].get
                )
                if random.random() < epsilon:
                    next_action = np.random.choice(
                        [
                            "up", 
                            "down", 
                            "left", 
                            "right"
                        ]
                    )
                Qfunction[state][action] += (
                    step_size * (
                        reward + 
                        gamma * (
                            Qfunction[next_state][next_action] 
                        )
                        - Qfunction[state][action]
                    )
                )
                state = next_state
                action = next_action

        self.display_q_function(Qfunction)  
    
    def sarsa_max(
            self, 
            epochs, 
            step_size, 
            gamma, 
            epsilon, 
            start_coordinates
        ):
        Qfunction = {}

        for _ in range(epochs):
            state = tuple(start_coordinates)
            if state not in list(Qfunction.keys()):
                Qfunction[state] = {
                    "up": 0,
                    "down": 0,
                    "left": 0,
                    "right": 0
                }

            while list(state) not in self.maze.terminal_states:
                action = max(Qfunction[state], key=Qfunction[state].get)
                if random.random() < epsilon:
                    action = np.random.choice(
                        [
                            "up", 
                            "down", 
                            "left", 
                            "right"
                        ]
                    )
                
                next_state = self.maze.step(state, action)

                reward = self.maze.maze[next_state[0]][next_state[1]]
                if next_state not in list(Qfunction.keys()):
                    Qfunction[next_state] = {
                        "up": 0, 
                        "down": 0,
                        "left": 0,
                        "right": 0
                    }
                next_action = max(
                    Qfunction[next_state], 
                    key=Qfunction[next_state].get
                )
                Qfunction[state][action] += (
                    step_size * (
                        reward + 
                        gamma * (
                            Qfunction[next_state][next_action] 
                        )
                        - Qfunction[state][action]
                    )
                )
                state = next_state
        self.display_q_function(Qfunction)    
        
            
    def display_q_function(self, Qfunction):
        window_size = 1000
        border_width = 1

        cell_size = (window_size // len(self.maze.maze[0]), window_size// len(self.maze.maze))
        pygame.init()

        screen = pygame.display.set_mode((1000, 1000), pygame.DOUBLEBUF)
        colors = { 
            -1: (255, 255, 255), 
            -2: (0, 0, 255),
            -10: (255, 0, 0), 
            10: (0, 255, 0), 
            40: (0, 255, 255) } 
        running = True
        font = pygame.font.Font(None, 24)  # Font for rendering text
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    CONTINUE = False
            #Display the maze
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # screen.fill([255,255,255])
            for state in Qfunction.keys():

                pygame.draw.rect(
                    screen,  
                    (255, 255, 255),
                    pygame.Rect(
                        state[0] * cell_size[0], 
                        state[1] * cell_size[1], 
                        cell_size[0] - border_width, 
                        cell_size[1] - border_width
                    )
                )
                font = pygame.font.SysFont(None, 25)
                positions = {
                    'up': (state[0] * cell_size[0] + cell_size[0] / 2, state[1] * cell_size[1] + cell_size[1] / 4),
                    'down': (state[0] * cell_size[0] + cell_size[0] / 2, state[1] * cell_size[1] + 3 * cell_size[1] / 4),
                    'left': (state[0] * cell_size[0] + cell_size[0] / 4, state[1] * cell_size[1] + cell_size[1] / 2),
                    'right': (state[0] * cell_size[0] + 3 * cell_size[0] / 4, state[1] * cell_size[1] + cell_size[1] / 2),
                }

                for action, value in Qfunction[(state[1], state[0])].items():
                    value_text = font.render("{:.2f}".format(value), True, (0, 0, 0))
                    text_rect = value_text.get_rect()
                    text_rect.center = positions[action]
                    screen.blit(value_text, text_rect)

                center = (state[0] * cell_size[0] + cell_size[0] / 2, state[1] * cell_size[1] + cell_size[1] / 2)
                corners = {
                    'up': (state[0] * cell_size[0], state[1] * cell_size[1]),
                    'down': (state[0] * cell_size[0] + cell_size[0], state[1] * cell_size[1] + cell_size[1]),
                    'left': (state[0] * cell_size[0], state[1] * cell_size[1] + cell_size[1]),
                    'right': (state[0] * cell_size[0] + cell_size[0], state[1] * cell_size[1]),
                }

                for corner in corners.values():
                    pygame.draw.line(screen, (0, 0, 0), center, corner, 1)

                pygame.display.update()
                # Display the policy values and directions
        

            pygame.display.flip()
    