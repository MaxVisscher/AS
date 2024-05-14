import pygame
from maze import Maze
from agent import Agent
from randomPolicy import RandomPolicy
from ValueIterationPolicy import ValueIterationPolicy


def display(Agent, maze, border_width = 5, window_size = (1000,1000)):
    cell_size = (window_size[1] // len(maze.maze[0]), window_size[1]// len(maze.maze))
    pygame.init()
  
    screen = pygame.display.set_mode((1000, 1000))
    colors = { -1: (255, 255, 255), -2: (0, 0, 255), -10: (255, 0, 0), 10: (0, 255, 0), 40: (0, 255, 255) }
    agent_color = (0, 0, 0)  
    agent_radius = 20 
    running = True
    finished = False

    while running:
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
        #Display the agent
        pygame.draw.circle(
            screen, 
            agent_color, 
            (
                Agent.current_state[1] * cell_size[0] + cell_size[0] // 2, 
                Agent.current_state[0] * cell_size[1] + cell_size[1] // 2), 
                agent_radius
            )
        #Display the score
        font = pygame.font.SysFont(None, 500)
        text_surf = font.render(str(Agent.reward), True, (0, 0, 0))
        text_surf.set_alpha(127)
        screen.blit(text_surf, (50, 325))

        pygame.display.flip()
       
        if finished:
            pygame.time.wait(5000)
            Agent.current_state = [3,2]  
            # running = False     
        else:
            Agent.act()
            
            print(Agent.policy.values)
            break
            pygame.time.wait(500)  
            if Agent.current_state in maze.terminal_states:
                print("You have reached the goal!")
                finished = True
                
            
    pygame.quit()

def main():
    maze = Maze()
    # Policy = RandomPolicy()
    Policy = ValueIterationPolicy(maze)
    Bozo = Agent(maze, Policy, maze.start_coordinates)
    display(Bozo, maze)

if __name__ == "__main__":
    main()

       