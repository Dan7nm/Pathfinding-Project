import pygame 
import algorithms

# Constants:
WIDTH = 200
HEIGHT = 200
BLOCK_SIZE = 20
FPS = 60

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

# Main function
def main():
    # Initialize pygame
    pygame.init()

    # Initilize if mouse was clicked
    mouse_clicked = False

    # Initilize start,end point was not chosen
    starting_point_chosen = False
    ending_point_chosen = False

    # Initialize grid
    grid = init_grid()

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(BLACK)

    running = True
    while running:
        # Limit the app to 60 fps
        clock.tick(FPS)

        # Loop checks for every event happening on the screen
        for event in pygame.event.get():
            # If the window was closed quit the app 
            if event.type==pygame.QUIT:
                running = False
            # Draw a square in the place mouse was clicked
            elif event.type==pygame.MOUSEBUTTONDOWN:
                # Check if start,point was chosen else draw a white square
                if not starting_point_chosen:
                    draw_square(pygame.mouse.get_pos(),screen,GREEN)
                    starting_point_chosen = True
                    grid = update_grid('start',pygame.mouse.get_pos(),grid)
                elif not ending_point_chosen:
                    draw_square(pygame.mouse.get_pos(),screen,RED)
                    ending_point_chosen = True
                    grid = update_grid('end',pygame.mouse.get_pos(),grid)
                else:
                    draw_square(pygame.mouse.get_pos(),screen,WHITE)
                    mouse_clicked = True
                    grid = update_grid('1',pygame.mouse.get_pos(),grid)
            elif event.type==pygame.MOUSEMOTION and mouse_clicked==True:
                draw_square(pygame.mouse.get_pos(),screen,WHITE)
                grid = update_grid('1',pygame.mouse.get_pos(),grid)
            elif event.type==pygame.MOUSEBUTTONUP:
                mouse_clicked=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    print_grid(grid)

        # Draw the grid
        draw_grid(screen)

        # Update the screen with the drawn objects
        pygame.display.update()


    # Quit the app
    pygame.quit()


# This function draws the grid
def draw_grid(screen):
    for x in range(0,WIDTH,BLOCK_SIZE):
        for y in range(0,HEIGHT,BLOCK_SIZE):
            rect = pygame.Rect(x,y,BLOCK_SIZE,BLOCK_SIZE)
            pygame.draw.rect(screen,WHITE,rect,1)

# Draw a square when mouse was clicked
def draw_square(pos,screen,color):
    mouse_x,mouse_y=pos
    mouse_x //= BLOCK_SIZE
    mouse_y //= BLOCK_SIZE
    rect = pygame.Rect(mouse_x*BLOCK_SIZE,mouse_y*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)
    pygame.draw.rect(screen,color,rect)

# Initialize the grid for the algorithm
# start - means the square is the starting point
# end - this square is the goal 
# empty - empty square and allowed to travel
# obstacle - means you can travel through this square
# we will initialize the grid to empty everything
def init_grid():
    grid = []
    for x in range(0,WIDTH,BLOCK_SIZE):
        row = []
        for y in range(0,HEIGHT,BLOCK_SIZE):
            row.append('0')
        grid.append(row)
    return grid

# Print the grid 
def print_grid(grid):
    for row in grid:
        row_string = ''
        for element in row:
            row_string+=' '+element+' '
        print(row_string)

# Updates the grid with the user actions
def update_grid(action,pos,grid):
    x_pos = pos[0]//BLOCK_SIZE
    y_pos = pos[1]//BLOCK_SIZE
    grid[y_pos][x_pos] = action
    return grid

# Run Main function
if __name__ == '__main__':
    main()
    # print_grid(init_grid())
    print('------------ Quiting Program ------------')
