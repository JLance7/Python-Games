#This is a pong game for learning pygame
#IMPORTS
import pygame
import random
import sys
import os
from pygame import mixer
from pygame.locals import *

#CONSTANTS
#pygame.mixer.init(48000, -16, 2, 1024)
pygame.init()
pygame.font.init()
pygame.display.set_caption("Pong")
WIDTH, HEIGHT = 900, 500
FPS = 60
VEL = 10
#set window
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
#set background as black rectangle (x, y, width, height)
BACKGROUND = pygame.Rect(0, 0, WIDTH, HEIGHT)  
#middle border
BORDER = pygame.Rect(WIDTH//2 - 4, 0, 8, HEIGHT)
PLAYER_HEIGHT = 100
PLAYER_WIDTH = 15
BALL_SIDE = 10

#sounds
hit = os.path.join('resources', 'hit.wav')
hit_sound = pygame.mixer.Sound(hit)

#FONTS
POINTS_FONT = pygame.font.SysFont('Bahnschrift', 40)
WINNER_FONT = pygame.font.SysFont('Bahnschrift', 100)

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#EVENTS
HORIZONTAL_HIT = pygame.USEREVENT + 1
VERTICAL_HIT = pygame.USEREVENT + 2
P1_POINT = pygame.USEREVENT + 3
P2_POINT = pygame.USEREVENT + 4


#get starting velocity for ball
def getBallStartVel():
    ballx = None
    bally = None
    num = random.randrange(1, 4)

    if num == 1:
        ballx = 6
        bally = 6
    elif num == 2:
        ballx = -6
        bally = 6
    elif num == 3:
        ballx = 6
        bally = -6
    elif num == 4:
        ballx = -6
        bally = -6
    list = [ballx, bally]
    print('ball x velocity is: ' + str(ballx))
    print('ball y velocity is: ' + str(bally))
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
                run = False
                pygame.quit()
                sys.exit() 

            if event.type == P1_POINT:
                p1_points += 1
                #reset ball to middle
                ball.x = (WIDTH//2 - BALL_SIDE//2)
                ball.y = (HEIGHT//2 - BALL_SIDE//2)
                ball_x_velocity = -(ballVel[0])
                ball_y_velocity = -(ballVel[1])
                pygame.time.delay(1000)

            if event.type == P2_POINT:
                p2_points += 1
                #reset ball to middle
                ball.x = (WIDTH//2 - BALL_SIDE//2)
                ball.y = (HEIGHT//2 - BALL_SIDE//2)
                ball_x_velocity = -(ballVel[0])
                ball_y_velocity = -(ballVel[1])
                pygame.time.delay(1000)
            
            if event.type == VERTICAL_HIT:
                ball_y_velocity = -(ball_y_velocity + 1)
                
            
            if event.type == HORIZONTAL_HIT:
                ball_x_velocity = -(ball_x_velocity + 2)
                

        if p1_points >= 10:
            p1Win = True
        if p2_points >= 10:
            p2Win = True
        if p1Win:
            winScreen('p1')
            break
        if p2Win:
            winScreen('p2')
            break


        keys_pressed = pygame.key.get_pressed()        
        handlePlayerMovement(keys_pressed, player1rect, player2rect)
        handleBallMovement(ball, ball_x_velocity, ball_y_velocity, player1rect, player2rect)      
        draw(player1rect, player2rect, ball, p1_points, p2_points)

    main()

def draw(player1rect, player2rect, ball, p1_points, p2_points):
    p1_text = POINTS_FONT.render(str(p1_points), 1, WHITE)
    p2_text = POINTS_FONT.render(str(p2_points), 1, WHITE)
    #draw black rectangle as background (window, color, rectangle)
    pygame.draw.rect(WIN, BLACK, BACKGROUND)
    pygame.draw.rect(WIN, WHITE, BORDER)
    WIN.blit(p1_text, ((20, 20)))
    WIN.blit(p2_text, ((WIDTH - p2_text.get_width() - 20, 20)))
    pygame.draw.rect(WIN, WHITE, player1rect)
    pygame.draw.rect(WIN, WHITE, player2rect)
    pygame.draw.rect(WIN, WHITE, ball)

    pygame.display.update()



def handlePlayerMovement(keys_pressed, player1rect, player2rect):
    #player 1 movement
    #up
    if (keys_pressed[pygame.K_w] or keys_pressed[pygame.K_a]) and player1rect.y - VEL > 0:
        player1rect.y -= VEL
    #down
    if (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_s]) and player1rect.y + VEL + PLAYER_HEIGHT < HEIGHT:
        player1rect.y += VEL

    #player 2 movement
    if (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_LEFT]) and player2rect.y - VEL > 0:
        player2rect.y -= VEL
    if (keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_DOWN]) and player2rect.y + VEL + PLAYER_HEIGHT < HEIGHT:
        player2rect.y += VEL


#handle movement of ball
def handleBallMovement(ball, ball_x_movement, ball_y_movement, player1, player2):
    #advance x and y velocities for ball
    ball.x += ball_x_movement
    ball.y += ball_y_movement

    #if ball hits player1 or player2
    if ball.colliderect(player1) or ball.colliderect(player2):
        pygame.event.post(pygame.event.Event(HORIZONTAL_HIT))
        hit_sound.play()
    
    #if ball hits top
    if ball.y + ball_y_movement <= 1:
        pygame.event.post(pygame.event.Event(VERTICAL_HIT))
        hit_sound.play()

    #if ball hits bottom
    if ball.y + ball_y_movement >= HEIGHT-1:
        pygame.event.post(pygame.event.Event(VERTICAL_HIT))
        hit_sound.play()

    #if goes out of bounds to left 
    if ball.x > WIDTH:
        pygame.event.post(pygame.event.Event(P1_POINT))

    #if goes out of bounds to left 
    if ball.x < 0:
        pygame.event.post(pygame.event.Event(P2_POINT))


def startScreen():
    clock = pygame.time.Clock()
    text = "Press SPACE to start"
    playText = POINTS_FONT.render(text, 1, WHITE)

    #music
    #background = os.path.join('resources', 'background.wav')
    #mixer.music.load(background)
    #mixer.music.play(-1)

    pygame.draw.rect(WIN, BLACK, BACKGROUND)
    WIN.blit(playText, ((WIDTH//2 - playText.get_width()//2, HEIGHT//2 - playText.get_height()//2)))
    pygame.display.update()  

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
                    main()
            

def winScreen(player):
    clock = pygame.time.Clock()
    winner = ""
    playAgain = "Press SPACE to playagain or 'q' to quit"
    if player == 'p1':
        winner = "Player 1 Wins!"
    else:
        winner = "Player 2 Wins!"

    winnerText = WINNER_FONT.render(winner, 1, WHITE)
    playText = POINTS_FONT.render(playAgain, 1, WHITE)

    pygame.draw.rect(WIN, BLACK, BACKGROUND)
    WIN.blit(winnerText, ((WIDTH//2 - winnerText.get_width()//2, HEIGHT//2 - winnerText.get_height()//2 - 100)))
    WIN.blit(playText, ((WIDTH//2 - playText.get_width()//2, HEIGHT//2 - playText.get_height()//2 + 100)))
    pygame.display.update()
    pygame.time.delay(1000)
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
                elif event.key == pygame.K_q:
                    run = False
                    pygame.quit()
                    sys.exit()
        
        



if __name__ == '__main__':
    startScreen()