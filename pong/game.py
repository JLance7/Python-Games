#This is a pong game for learning pygame
#IMPORTS
import pygame

#CONSTANTS
pygame.display.set_caption("Pong")
WIDTH, HEIGHT = 900, 500
FPS = 60
VEL = 5
#set window
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
#set background as black rectangle (x, y, width, height)
BACKGROUND = pygame.Rect(0, 0, WIDTH, HEIGHT)  
#middle border
BORDER = pygame.Rect(WIDTH//2 - 2.5, 0, 5, HEIGHT)
PLAYER_HEIGHT = 150
PLAYER_WIDTH = 15

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


#main runner
def main():
    PLAYER1RECT = pygame.Rect(0 + 20, HEIGHT//2 - 75, PLAYER_WIDTH, PLAYER_HEIGHT)
    PLAYER2RECT = pygame.Rect(WIDTH - (15 + 20), HEIGHT//2 - 75, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        #set to 60 loops per second
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
            
        keys_pressed = pygame.key.get_pressed()        
        handlePlayerMovement(keys_pressed, PLAYER1RECT, PLAYER2RECT)      
        draw(PLAYER1RECT, PLAYER2RECT)


#draw to screen
def draw(PLAYER1RECT, PLAYER2RECT):
    #draw black rectangle as background (window, color, rectangle)
    pygame.draw.rect(WIN, BLACK, BACKGROUND)
    pygame.draw.rect(WIN, WHITE, BORDER)
    pygame.draw.rect(WIN, WHITE, PLAYER1RECT)
    pygame.draw.rect(WIN, WHITE, PLAYER2RECT)

    pygame.display.update()


#handle movement of player rectangles
def handlePlayerMovement(keys_pressed, PLAYER1RECT, PLAYER2RECT):
    #player 1 movement
    if (keys_pressed[pygame.K_w] or keys_pressed[pygame.K_a]) and PLAYER1RECT.y >= 0 + (PLAYER_HEIGHT//4):
        PLAYER1RECT.y -= VEL
    if (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_s]) and PLAYER1RECT.y <= HEIGHT - (PLAYER_WIDTH//2):
        PLAYER1RECT.y += VEL

    #player 2 movement
    if (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_LEFT]) and PLAYER2RECT.y >= 0 + (PLAYER_HEIGHT//4):
        PLAYER2RECT.y -= VEL
    if (keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_DOWN]) and PLAYER2RECT.y <= HEIGHT - (PLAYER_WIDTH//2):
        PLAYER2RECT.y += VEL





main()