import pygame 

# Constants:
WIDTH = 600
HEIGHT = 600
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
                elif not ending_point_chosen:
                    draw_square(pygame.mouse.get_pos(),screen,RED)
                    ending_point_chosen = True
                else:
                    draw_square(pygame.mouse.get_pos(),screen,WHITE)
                    mouse_clicked = True
            elif event.type==pygame.MOUSEMOTION and mouse_clicked==True:
                draw_square(pygame.mouse.get_pos(),screen,WHITE)
            elif event.type==pygame.MOUSEBUTTONUP:
                mouse_clicked=False

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


# Run Main function
if __name__ == '__main__':
    main()
    print('------------ Quiting Program ------------')
    