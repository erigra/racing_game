import pygame
from random import randint


# Load images



# Global variables
WIDTH, HEIGHT = 500, 500

pygame.init()
screen= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic pygame mal")
clock= pygame.time.Clock()
gui_font= pygame.font.Font(None,30)


# Colors
BACKGROUND_COLOR = (255,255,255)




# Main loop ::::::::::::::::::::::::::::::::::::::::::::::::::::

def main():
    
    
    
    
    
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill(BACKGROUND_COLOR)

        pygame.display.update()
        clock.tick(60)



if __name__== "__main__":
    main()




