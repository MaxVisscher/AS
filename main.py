import pygame
from maze import Maze
from agent import Agent
from randomPolicy import RandomPolicy
from ValueIterationPolicy import ValueIterationPolicy
from temporal import TemporalDiff
from SARSA import Sarsa

CONTINUE = True

def display(Agent : Agent, maze: Maze, border_width = 5, window_size = (1000,1000)):
    global CONTINUE

    cell_size = (window_size[1] // len(maze.maze[0]), window_size[1]// len(maze.maze))
    pygame.init()

    screen = pygame.display.set_mode((1000, 1000))
    colors = { 
        -1: (255, 255, 255), 
        -2: (0, 0, 255),
        -10: (255, 0, 0), 
        10: (0, 255, 0), 
        40: (0, 255, 255) } 
    running = True
    finished = False
    agent_image = pygame.image.load('untitled.png')
    font = pygame.font.Font(None, 24)  # Font for rendering text
    terminal_image = pygame.image.load('untitled3.png')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                CONTINUE = False
        #Display the maze
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for i, row in enumerate(maze.maze):
            for j, cell in enumerate(row):
                pygame.draw.rect(
                    screen, 
                    colors[cell], 
                    pygame.Rect(
                        j * cell_size[0], 
                        i * cell_size[1], 
                        cell_size[0] - border_width, 
                        cell_size[1] - border_width
                    )
                )

                # Display the policy values and directions
                value = Agent.policy.values[i][j]
                direction = Agent.policy.p[i][j]
                font = pygame.font.SysFont(None, 50)
                value_text = font.render("{:.2f}".format(value), True, (0, 0, 0))
                direction_text = font.render(str(direction), True, (0, 0, 0))

                screen.blit(value_text, (j * cell_size[0] + 5, i * cell_size[1] + 5))
                screen.blit(direction_text, (j * cell_size[0] + 5, i * cell_size[1] + 30))

        #Display the agent
        screen.blit(
            agent_image, 
            (
                maze.agent_pos[1] * cell_size[0] + cell_size[0] // 2 - agent_image.get_width() // 2, 
                maze.agent_pos[0] * cell_size[1] + cell_size[1] // 2 - agent_image.get_height() // 2
            )
        )
        if maze.agent_pos not in maze.terminal_states:
           screen.blit(
                terminal_image, 
                (
                    3 * cell_size[0] + cell_size[0] // 2 - agent_image.get_width() // 2, 
                    0 * cell_size[1] + cell_size[1] // 2 - agent_image.get_height() // 2
                )
            )
        #Display the score
        font = pygame.font.SysFont(None, 500)
        text_surf = font.render(str(Agent.reward), True, (0, 0, 0))
        text_surf.set_alpha(127)
        # screen.blit(text_surf, (50, 325))

        pygame.display.flip()
       
        if finished:
            pygame.time.wait(5000)
            Agent.current_state = [3,2]  
            running = False     
        else:
            Agent.act()
            pygame.time.wait(500)  
            if maze.agent_pos in maze.terminal_states:
                agent_image = pygame.image.load('untitled2.png')
                print("You have reached the goal!")
                finished = True
                

def main():
    # while CONTINUE:
    maze = Maze()
    # Policy = RandomPolicy()
    Temp = ValueIterationPolicy(maze, gamma = 1)
    Optimal = Temp.p
    # td = TemporalDiff(Optimal, 1000, 1,maze, maze.start_coordinates)
    # td.temporal_difference(100000, Optimal, maze.start_coordinates, 0.1)
    Sar = Sarsa(maze, Temp, maze.start_coordinates)
    Bozo = Agent(maze, Temp, maze.start_coordinates)
    Sar.sarsa_max(350000, 0.1, 0.9, 0.1, maze.start_coordinates)
    # print(Optimal)
    # Policy.temporal_difference()
    # print(Policy.policy)
    # display(Bozo, maze)
    pygame.quit()

if __name__ == "__main__":
    main()

       