import pygame 
from queue import Queue,LifoQueue
import heapq
import math

# Constants:
WIDTH = 600
HEIGHT = 600
BLOCK_SIZE = 20
FPS = 60
GRID_WIDTH = 30
GRID_HEIGHT = 30

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
ORANGE = (255,165,0)
BLUE = (0,0,255)

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
            # convert mouse position to grid position
            grid_pos= cvt_coord(pygame.mouse.get_pos())

            # If the window was closed quit the app 
            if event.type==pygame.QUIT:
                running = False
            # Draw a square in the place mouse was clicked
            elif event.type==pygame.MOUSEBUTTONDOWN:
                # Save the starting point if it wasn't chosen
                if not starting_point_chosen:
                    starting_pos = grid_pos
                    draw_square(starting_pos,screen,GREEN)
                    starting_point_chosen = True
                # Save the ending point if it wasn't chosen
                elif not ending_point_chosen:
                    ending_pos = grid_pos
                    draw_square(ending_pos,screen,RED)
                    ending_point_chosen = True
                # Draw a white square that indicates an obstacle
                elif pygame.mouse.get_pos():
                    draw_square(grid_pos,screen,WHITE)
                    mouse_clicked = True
                    grid = update_grid(True,grid_pos,grid)
            # Draw white squares while the mouse button is pressed down
            elif event.type==pygame.MOUSEMOTION and mouse_clicked==True:
                draw_square(grid_pos,screen,WHITE)
                grid = update_grid(True,grid_pos,grid)
            # Reset the the var that checks if it is a continous click
            elif event.type==pygame.MOUSEBUTTONUP:
                mouse_clicked=False
            elif event.type==pygame.KEYDOWN:
                # Use bfs to search for the end point
                if event.key==pygame.K_b:
                    if bfs(grid,starting_pos,ending_pos,screen,clock):
                        print('Ending point was found using bfs')
                    else:
                        print('Ending point was not found')
                # Use dfs to find the end point
                if event.key==pygame.K_d:
                    if dfs(grid,starting_pos,ending_pos,screen,clock):
                        print('Ending point was found using dfs')
                    else:
                        print('Ending point was not found')
                # Use dijkstra to find the end point
                if event.key==pygame.K_j:
                    if dijkstra(grid,starting_pos,ending_pos,screen,clock):
                        print('Ending point was found using dijkstra')
                    else:
                        print('Ending point was not found')
                # Reset the grid if space was pressed
                if event.key==pygame.K_SPACE:
                    grid = init_grid()
                    starting_point_chosen = False
                    ending_point_chosen = False
                    screen.fill(BLACK)

        # Draw the grid
        draw_grid(screen)

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
    rect = pygame.Rect(mouse_x*BLOCK_SIZE,mouse_y*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)
    pygame.draw.rect(screen,color,rect)
    pygame.display.update()

# Initilize the whole grid to the given value
# Initialize the grid for the algorithm
# we will initialize the grid to false everything by default
# False means there is no obstacle or the algorithm has no visited there yet
# Starting point will also be True
def init_grid(value=False):
    grid = []
    for y in range(GRID_HEIGHT):
        row = []
        for x in range(GRID_WIDTH):
            row.append(value)
        grid.append(row)
    return grid

# Updates the grid with the user actions
def update_grid(action,pos,grid):
    x_pos,y_pos = pos
    grid[y_pos][x_pos] = action
    return grid

# Converts mouse coordinates to grid coordinates 
# Meaning we will know which square on the grid the mouse touches
def cvt_coord(mouse_pos):
    grid_x,grid_y=mouse_pos
    grid_x//=BLOCK_SIZE
    grid_y//=BLOCK_SIZE
    return (grid_x,grid_y)


# bfs search algorithm using queue
def bfs(grid,start,end,screen,clock):
    start_x,start_y=start
    queue = Queue()
    # Mark starting point as visited (True) on the grid
    grid[start_y][start_x]=True
    queue.put(start)
    while not queue.empty():
        # Limit the speed of the algorithm to see it's steps
        clock.tick(FPS)
        v = queue.get()
        # Draw orange squares to show visited squares by the algorithm
        # Do not draw on the starting square to show the start point
        if v!=start:
            draw_square((v[0],v[1]),screen,ORANGE)
        if v==end:
            return True
        for (x_pos,y_pos) in get_neighbours(grid,v):
            # Mark the square as visited
            grid[y_pos][x_pos]=True
            queue.put((x_pos,y_pos))
    return False


# Dfs search algorithm using stack
def dfs(grid,start,end,screen,clock):
    stack = LifoQueue()
    stack.put(start)
    while not stack.empty():
        clock.tick(FPS)
        v = stack.get()
        v_x,v_y = v
        # Draw orange squares to show visited squares by the algorithm
        # Do not draw on the starting square to show the start point
        if v!=start:
            draw_square((v[0],v[1]),screen,ORANGE)
        if v==end:
            return True
        # Mark the v square as visited if not already visited
        if not grid[v_y][v_x]:
            grid[v_y][v_x] = True
            for neighbour in get_neighbours(grid,v):
                stack.put(neighbour)
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
                if grid[neighbour_y][neighbour_x]==False and point!=(x,y):
                    neighbours.append((neighbour_x,neighbour_y))
    return neighbours

# Find the shortest path using Dijkstra using heap
def dijkstra(grid,start,end,screen,clock):
    heap = []
    # We initlize a grid with each square containing a tuple of the prevous square
    prev = init_grid(0)
    # We initialize all the the squares to be infinite distance
    dist = init_grid(math.inf)
    start_x,start_y = start
    # We initialize the starting position to zero distance
    dist[start_y][start_x] = 0
    # We push the start point into the heap
    heapq.heappush(heap,(dist[start_y][start_x],(start_x,start_y)))
    while heap:
        clock.tick(FPS)
        # pop the the pos of the quare with min distance
        u = heapq.heappop(heap)[1]
        u_x,u_y = u
        # Draw orange squares to show visited squares by the algorithm
        # Do not draw on the starting square to show the start point
        if u==end:
            print_shortest_path(prev,start,end,screen)
            return True
        if u!=start:
            draw_square(u,screen,ORANGE)
        for neighbour in get_neighbours(grid,u):
            neighbour_x,neighbour_y = neighbour
            alt = dist[u_y][u_x]+1
            if alt < dist[neighbour_y][neighbour_x]:
                dist[neighbour_y][neighbour_x] = alt
                prev[neighbour_y][neighbour_x] = (u_x,u_y)
                heapq.heappush(heap,(dist[neighbour_y][neighbour_x],(neighbour_x,neighbour_y)))
    return False

# Prints the shortest path
def print_shortest_path(prev,start,end,screen):
    end_x,end_y = end
    # Set the current square as the previous one to ending 
    curr = prev[end_y][end_x]
    # While loop that draws all previous square from the ending square
    # Thus printing in the end the shortest path from start to end
    while curr!=start:
        curr_x,curr_y=curr
        draw_square(curr,screen,BLUE)
        curr = prev[curr_y][curr_x]

    
# Run Main function
if __name__ == '__main__':
    main()
    print('------------ Quiting Program ------------')
