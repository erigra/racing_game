from turtle import Screen
import pygame
from random import randint

class Car():
    def __init__(self, speed, pos):       
        self.speed = speed
        self.pos = pos
        self.in_lane = True


# Load images + scale & rotate




# Global variables
WIDTH, HEIGHT = 500, 1000
player_car_speed = 5

LANE_POSITIONS = [80, 230, 380]


pygame.init()
SCREEN= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic pygame mal")
clock= pygame.time.Clock()
gui_font= pygame.font.Font(None,30)


# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

# FUnctions ------------------------------------------------------------------------------
def handle_player_car_movement(change_lane, player_car): 
    if player_car.in_lane == False:
        if change_lane == "left" and player_car.pos.x != LANE_POSITIONS[0]:
            player_car.pos.x -= 10
        if change_lane == "right" and player_car.pos.x != LANE_POSITIONS[2]:
            player_car.pos.x += 10
           
def check_car_position(player_car):
    if player_car.pos.x in LANE_POSITIONS:
        player_car.in_lane = True
    



def update_screen(SCREEN, player_car):
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, RED, player_car.pos)
    pygame.display.update()


# Main loop ::::::::::::::::::::::::::::::::::::::::::::::::::::

def main():
    
    change_lane=""
    player_pos = pygame.Rect(280, 800, 40, 100)
    player_car = Car(2,player_car_speed, player_pos)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_lane = "left"
                    player_car.in_lane = False
                if event.key == pygame.K_RIGHT:
                    change_lane = "right"
                    player_car.in_lane = False


         
        
        
        handle_player_car_movement(change_lane, player_car)
        check_car_position(player_car)

        print(player_car.pos.x)                                                 # Debug code
        update_screen(SCREEN, player_car)
        clock.tick(60)

if __name__== "__main__":
    main()




