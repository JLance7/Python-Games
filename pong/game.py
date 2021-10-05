#This is a pong game for learning pygame
#IMPORTS
import pygame
import random

#CONSTANTS
pygame.init()
pygame.display.set_caption("Pong")
WIDTH, HEIGHT = 900, 500
FPS = 60
VEL = 5
#set window
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
#set background as black rectangle (x, y, width, height)
BACKGROUND = pygame.Rect(0, 0, WIDTH, HEIGHT)  
#middle border
BORDER = pygame.Rect(WIDTH//2 - 4, 0, 8, HEIGHT)
PLAYER_HEIGHT = 100
PLAYER_WIDTH = 15
BALL_SIDE = 5

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#EVENTS
HORIZONTAL_HIT = pygame.USEREVENT + 1
VERTICAL_HIT = pygame.USEREVENT + 3
P1_POINT = pygame.USEREVENT + 7
P2_POINT = pygame.USEREVENT + 8


#get starting velocity for ball
def getBallStartVel():
    ballx = None
    bally = None
    num = random.randrange(1, 4)
    if num == 1:
        ballx = 5
        bally = 5
    elif num == 2:
        ballx = -5
        bally = 5
    elif num == 2:
        ballx = 5
        bally = -5
    elif num == 2:
        ballx = -5
        bally = -5
    print('Ball starting x is: ' + ballx)
    print('Ball starting y is: ' + bally)
    list = [ballx, bally]
    return list


#main runner
def main():
    clock = pygame.time.Clock()
    player1rect = pygame.Rect(0 + 20, HEIGHT//2 - (PLAYER_HEIGHT//2), PLAYER_WIDTH, PLAYER_HEIGHT)
    player2rect = pygame.Rect(WIDTH - (PLAYER_WIDTH + 20), HEIGHT//2 - (PLAYER_HEIGHT//2), PLAYER_WIDTH, PLAYER_HEIGHT)
    ball = pygame.Rect(WIDTH//2 - BALL_SIDE//2, HEIGHT//2 - BALL_SIDE//2, BALL_SIDE, BALL_SIDE)
    ballVel = getBallStartVel()
    ball_x_velocity = ballVel[0]
    ball_y_velocity = ballVel[1]
    print(ball_y_velocity)
    print(ball_y_velocity)
    p1_points = 0
    p2_points = 0
    p1Win = False
    p2Win = False

    run = True
    while run:
        #set to 60 loops per second
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 

            if event.type == P1_POINT:
                p1_points += 1

            if event.type == P2_POINT:
                p2_points += 1

        if p1_points >= 10:
            p1Win = True
        if p2_points >= 10:
            p2Win = True
        if p1Win or p2Win:
            pass


        keys_pressed = pygame.key.get_pressed()        
        handlePlayerMovement(keys_pressed, player1rect, player2rect)
        handleBallMovement(ball, ball_x_velocity, ball_y_velocity, player1rect, player2rect)      
        draw(player1rect, player2rect, ball)



def draw(player1rect, player2rect, ball):
    #draw black rectangle as background (window, color, rectangle)
    pygame.draw.rect(WIN, BLACK, BACKGROUND)
    pygame.draw.rect(WIN, WHITE, BORDER)
    pygame.draw.rect(WIN, WHITE, player1rect)
    pygame.draw.rect(WIN, WHITE, player2rect)
    pygame.draw.rect(WIN, WHITE, ball)

    pygame.display.update()



def handlePlayerMovement(keys_pressed, player1rect, player2rect):
    #player 1 movement
    if (keys_pressed[pygame.K_w] or keys_pressed[pygame.K_a]) and player1rect.y - VEL > 0:
        player1rect.y -= VEL
    if (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_s]) and player1rect.y + VEL + PLAYER_HEIGHT < HEIGHT:
        player1rect.y += VEL

    #player 2 movement
    if (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_LEFT]) and player2rect.y - VEL > 0:
        player2rect.y -= VEL
    if (keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_DOWN]) and player2rect.y + VEL + PLAYER_HEIGHT < HEIGHT:
        player2rect.y += VEL


#handle movement of ball
def handleBallMovement(ball, ball_x_movement, ball_y_movement, player1, player2):
    #if ball hits player1 or player2
    if ball.colliderect(player1) or ball.colliderect(player2):
        pygame.event.post(pygame.event.Event(HORIZONTAL_HIT))
    
    #if ball hits top
    if ball.y + BALL_SIDE <= 0
    
    #if ball hits bottom

    #if goes out of bounds to left or right
    

# HORIZONTAL_HIT = pygame.USEREVENT + 1
# VERTICAL_HIT = pygame.USEREVENT + 3
# P1_POINT = pygame.USEREVENT + 7
# P2_POINT = pygame.USEREVENT + 8

if __name__ == '__main__':
    main()