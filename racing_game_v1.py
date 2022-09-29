import pygame
from random import randint
import os

class Car():
    def __init__(self, speed, pos):       
        self.speed = speed
        self.pos = pos
        self.in_lane = True


# Load images + scale & rotate
PLAYER_CAR_IMAGE=pygame.image.load(os.path.join("Graphics","player_car.png"))
PLAYER_CAR = pygame.transform.scale(PLAYER_CAR_IMAGE, (50,100))


# Global variables
WIDTH, HEIGHT = 500, 1000
player_car_speed = 8
LANE_CHANGE_SPEED = 5
LANE_POSITIONS = [90, 230, 370]
MAX_MARKINGS = 15
MARK = pygame.USEREVENT + 1

pygame.init()
SCREEN= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing game!")
clock= pygame.time.Clock()
gui_font= pygame.font.Font(None,30)

pygame.time.set_timer(MARK, 300)      # Setter en timer for event MARK inn i køen hvert 0,5 sekund

GREEN_L = pygame.Rect(0, 0, 50, HEIGHT)
GREEN_R = pygame.Rect(WIDTH-50, 0, 50, HEIGHT)
STRIPE_L = pygame.Rect(45,0,10,HEIGHT)
STRIPE_R = pygame.Rect(WIDTH-55,0,10,HEIGHT)
 
# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
ORANGE = (255,215,0)
GREEN = (0,120,0)

# Functions ------------------------------------------------------------------------------
def handle_player_car_movement(change_lane, player_car): 
    if player_car.in_lane == False:
        if change_lane == "left" and player_car.pos.x != LANE_POSITIONS[0]:
            player_car.pos.x -= LANE_CHANGE_SPEED
        if change_lane == "right" and player_car.pos.x != LANE_POSITIONS[2]:
            player_car.pos.x += LANE_CHANGE_SPEED
    if player_car.pos.x in LANE_POSITIONS:
        player_car.in_lane = True
    
def road_marker_movement(road_markings1, road_markings2, speed):
    for markers in road_markings1:
        markers.y += speed 
        if markers.y > HEIGHT:
            road_markings1.remove(markers)
    for markers in road_markings2:
        markers.y += speed
        if markers.y > HEIGHT:
            road_markings2.remove(markers)


def update_screen(SCREEN, player_car, road_markings1, road_markings2):
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, GREEN, GREEN_L)
    pygame.draw.rect(SCREEN, GREEN, GREEN_R)
    pygame.draw.rect(SCREEN, ORANGE, STRIPE_R)
    pygame.draw.rect(SCREEN, ORANGE, STRIPE_L)
    
    for marker in road_markings1:
        pygame.draw.rect(SCREEN, WHITE, marker)
    for marker in road_markings2:
        pygame.draw.rect(SCREEN, WHITE, marker)
    
    
    SCREEN.blit(PLAYER_CAR, (player_car.pos.x,player_car.pos.y))
    pygame.display.update()


# Main loop ::::::::::::::::::::::::::::::::::::::::::::::::::::

def main():
    
    change_lane=""
    player_pos = pygame.Rect(280, 800, 40, 100)
    player_car = Car(player_car_speed, player_pos)
    


    road_markings1=[]
    road_markings2=[]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and player_car.in_lane:
                if event.key == pygame.K_LEFT:
                    change_lane = "left"
                    player_car.in_lane = False
                if event.key == pygame.K_RIGHT and player_car.in_lane:
                    change_lane = "right" 
                    player_car.in_lane = False
                
        
            if event.type == pygame.USEREVENT+1:
                    if len(road_markings1)< MAX_MARKINGS:           
                        marker1 = pygame.Rect(180,0,8,50)            
                        road_markings1.append(marker1)
                        marker2 = pygame.Rect(320,0,8,50)            
                        road_markings2.append(marker2)
        
        
        
        
        road_marker_movement(road_markings1, road_markings2, player_car.speed) 
        
        handle_player_car_movement(change_lane, player_car)
                                              
        update_screen(SCREEN, player_car, road_markings1, road_markings2)
        clock.tick(60)

if __name__== "__main__":
    main()




