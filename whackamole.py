import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_pos = (0, 0)
        mole_size = mole_image.get_width()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                #check if the mole is clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos #get the mouse position
                    mole_rect = pygame.Rect(mole_pos[0], mole_pos[1], mole_size, mole_size) #create a rect for the mole

                    #check if the mouse is inside the mole rect
                    if mole_rect.collidepoint(mouse_x, mouse_y): #if the mouse is inside the mole rect, move the mole to a new position
                        mole_pos = (random.randint(0, 19) * 32, random.randint(0, 15) * 32)
                    
            screen.fill("light green")
            #draw the grid
            for i in range(0, 640, 32):
                pygame.draw.line(screen, "black", (i, 0), (i, 512))
            for j in range(0, 512, 32):
                pygame.draw.line(screen, "black", (0, j), (640, j))
            #draw the mole
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_pos))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
