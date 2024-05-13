import numpy as np
import pygame
from maze import Maze
from Agent import Agent
from Random import Random

def display(Agent, maze, border_width = 5, window_size = (1000,1000)):
    cell_size = (window_size[1] // len(maze[0]), window_size[1]// len(maze))
    pygame.init()
  
    screen = pygame.display.set_mode((1000, 1000))
    colors = { -1: (255, 255, 255), -2: (0, 0, 255), -10: (255, 0, 0), 10: (0, 255, 0), 40: (0, 255, 255) }
    agent_color = (0, 0, 0)  # color of the agent
    agent_radius = 20  # radius of the agent
    running = True
    finished = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for i, row in enumerate(maze):
            for j, cell in enumerate(row):
                pygame.draw.rect(screen, colors[cell], pygame.Rect(j*cell_size[0], i*cell_size[1], cell_size[0] - border_width, cell_size[1] - border_width))
        # draw the agent
        pygame.draw.circle(screen, agent_color, (Agent.current_pos[1]*cell_size[0] + cell_size[0]//2, Agent.current_pos[0]* cell_size[1] + cell_size[1]//2), agent_radius)
        font = pygame.font.SysFont(None, 500)

        text_surf = font.render(str(Agent.reward), True, (0, 0, 0))
        text_surf.set_alpha(127)

        screen.blit(text_surf, (50, 325))
        pygame.display.flip()
        print(Agent.reward)
        if finished:
            pygame.time.wait(5000)  
            running = False
        else:
            direction = Agent.pick_move()
            print(direction)
            pygame.time.wait(500)  
            if Agent.step(direction):
                print("You have reached the goal!")
                print(Agent.visited)
                finished = True
            
    pygame.quit()

def main():
    maze = Maze()
    Bozo = Random(maze.maze, maze.start_coordinates)
    display(Bozo, maze.maze)

if __name__ == "__main__":
    main()

       