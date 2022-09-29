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
player_car_speed = 10
LANE_CHANGE_SPEED = 5
LANE_POSITIONS = [80, 230, 380]
MAX_MARKINGS = 15
MARK = pygame.USEREVENT + 1

pygame.init()
SCREEN= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic pygame mal")
clock= pygame.time.Clock()
gui_font= pygame.font.Font(None,30)

pygame.time.set_timer(MARK, 500)

 
# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

# FUnctions ------------------------------------------------------------------------------
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
    
    for marker in road_markings1:
        pygame.draw.rect(SCREEN, WHITE, marker)
    for marker in road_markings2:
        pygame.draw.rect(SCREEN, WHITE, marker)
    
    pygame.draw.rect(SCREEN, RED, player_car.pos)
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_lane = "left"
                    player_car.in_lane = False
                if event.key == pygame.K_RIGHT:
                    change_lane = "right" 
                    player_car.in_lane = False                 
        
            if event.type == pygame.USEREVENT+1:
                    if len(road_markings1)< MAX_MARKINGS:           
                        marker1 = pygame.Rect(200,0,8,50)            
                        road_markings1.append(marker1)
                        marker2 = pygame.Rect(300,0,8,50)            
                        road_markings2.append(marker2)
        
        
        
        
        road_marker_movement(road_markings1, road_markings2, player_car_speed) 
        
        
        handle_player_car_movement(change_lane, player_car)
        # check_car_position(player_car)

        print(player_car.pos.x)                                                 # Debug code
        update_screen(SCREEN, player_car, road_markings1, road_markings2)
        clock.tick(60)

if __name__== "__main__":
    main()




