import pygame 
from queue import Queue

# Constants:
WIDTH = 600
HEIGHT = 600
BLOCK_SIZE = 20
FPS = 60
GRID_WIDTH = WIDTH//BLOCK_SIZE
GRID_HEIGHT = HEIGHT//BLOCK_SIZE

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
ORANGE = (255,165,0)

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

    # Initialize the display and the clock
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
                    starting_pos = pygame.mouse.get_pos()
                    draw_square(starting_pos,screen,GREEN)
                    starting_point_chosen = True
                elif not ending_point_chosen:
                    ending_pos = pygame.mouse.get_pos()
                    draw_square(ending_pos,screen,RED)
                    ending_point_chosen = True
                elif pygame.mouse.get_pos():
                    draw_square(pygame.mouse.get_pos(),screen,WHITE)
                    mouse_clicked = True
                    grid = update_grid(True,pygame.mouse.get_pos(),grid)
            elif event.type==pygame.MOUSEMOTION and mouse_clicked==True:
                draw_square(pygame.mouse.get_pos(),screen,WHITE)
                grid = update_grid(True,pygame.mouse.get_pos(),grid)
            elif event.type==pygame.MOUSEBUTTONUP:
                mouse_clicked=False
            elif event.type==pygame.KEYDOWN:
                # Print grid if p was pressed
                if event.key==pygame.K_p:
                    print_grid(grid)
                # If spacebar was pressed find the shortest path
                if event.key==pygame.K_SPACE:
                    if bfs(grid,starting_pos,ending_pos,screen,clock):
                        print('Ending point was found')
                    else:
                        print('Ending point was not found')

        # Draw the grid
        draw_grid(screen)

        # Update the screen with the drawn objects
        # pygame.display.update()

    # Quit the app
    pygame.quit()


# This function draws the grid
def draw_grid(screen):
    for x in range(0,WIDTH,BLOCK_SIZE):
        for y in range(0,HEIGHT,BLOCK_SIZE):
            rect = pygame.Rect(x,y,BLOCK_SIZE,BLOCK_SIZE)
            pygame.draw.rect(screen,WHITE,rect,1)
    pygame.display.update()


# Draw a square when mouse was clicked
def draw_square(pos,screen,color):
    mouse_x,mouse_y=pos
    mouse_x //= BLOCK_SIZE
    mouse_y //= BLOCK_SIZE
    rect = pygame.Rect(mouse_x*BLOCK_SIZE,mouse_y*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)
    pygame.draw.rect(screen,color,rect)
    pygame.display.update()


# Initialize the grid for the algorithm
# start - means the square is the starting point
# end - this square is the goal 
# empty - empty square and allowed to travel
# obstacle - means you can travel through this square
# we will initialize the grid to false everything
def init_grid():
    grid = []
    for x in range(0,WIDTH,BLOCK_SIZE):
        row = []
        for y in range(0,HEIGHT,BLOCK_SIZE):
            row.append(False)
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

# bfs search algorithm
def bfs(grid,start,end,screen,clock):
    start_x,start_y=start
    start_x//=BLOCK_SIZE
    start_y//=BLOCK_SIZE
    start = (start_x,start_y)
    end_x,end_y=end
    end_x//=BLOCK_SIZE
    end_y//=BLOCK_SIZE
    end = (end_x,end_y)
    queue = Queue()
    # Mark starting point as visited (True) on the grid
    grid[start[1]][start[0]]=True
    queue.put(start)
    while not queue.empty():
        clock.tick(FPS)
        v = queue.get()
        draw_square((v[0]*BLOCK_SIZE,v[1]*BLOCK_SIZE),screen,ORANGE)
        if v==end:
            return True
        for (x_pos,y_pos) in get_neighbours(grid,v):
            # Mark the square as visited
            grid[y_pos][x_pos]=True
            queue.put((x_pos,y_pos))
    return False

# Get all unexplored and not obstacle neighbours of a given square
def get_neighbours(grid,point):
    point_x,point_y=point
    neighbours = []
    for x in range(-1,2):
        for y in range(-1,2):
            neighbour_x = point_x+x
            neighbour_y = point_y+y
            if 0<=neighbour_x<GRID_WIDTH and 0<=neighbour_y<GRID_HEIGHT:
                if grid[neighbour_y][neighbour_x]==False:
                    neighbours.append((neighbour_x,neighbour_y))
    return neighbours


# Run Main function
if __name__ == '__main__':
    main()
    # print_grid(init_grid())
    print('------------ Quiting Program ------------')
