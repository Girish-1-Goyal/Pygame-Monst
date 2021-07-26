import pygame
import random
import sys
import math

pygame.init()

win = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space")

bg = pygame.image.load("bg.jpg")

playerimg = pygame.image.load("a.png")
playerX = 400
playerY = 10
player_change = 0

mostrimg = pygame.image.load("monster.png")
mostrX = random.randint(0,750)
mostrY = random.randint(350,550) 
mostrX_change = 1.5
mostry_change = 40

bombimg = pygame.image.load("bomb.png")
bombX = 400
bombY = 59
bombX_change = 0
bombY_change = 4
bomb_state = "ready"

score_value = 0
font = pygame.font.SysFont('times new roman',32,'italic')
x9 = 500
y9 = 0

def score(x,y):
    msg = font.render("Score:-" + str(score_value) ,True,(255,0,0))
    win.blit(msg,(x,y))

def player1(x,y):
    win.blit(playerimg,(x,y))

def mostr1(x,y):
    win.blit(mostrimg,(x,y))

def bomb1(x,y):
    global bomb_state
    bomb_state = "fire"
    win.blit(bombimg,(x+5,y+5))

def iscollision(mostrX,mostrY,bombX,bombY):
    d = math.sqrt((math.pow(mostrX-bombX,2)) + (math.pow(mostrY-bombY,2)))
    if d < 50:
        return True
    else:
        return False

run = True
while run:
    win.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_change = -3
    if keys[pygame.K_RIGHT]:
        player_change = +3
    if keys[pygame.K_DOWN]:
        player_change = 0
    if keys[pygame.K_SPACE]:
        if bomb_state is "ready":
            bombX = playerX
            bomb1(bombX,bombY)

    playerX += player_change
    player1(playerX,playerY)
    if playerX <= 0:
        playerX = 736
    elif playerX >= 736:
        playerX = 0

    mostrX += mostrX_change
    if mostrX <= 0:
        mostrX_change = 2
        mostrY -= mostry_change
    elif mostrX >= 736:
        mostrX_change = -2
        mostrY -= mostry_change
    mostr1(mostrX,mostrY)

    if bombY >= 570:
        bombY = 59
        bomb_state = "ready"
    if bomb_state is "fire":
        bomb1(bombX,bombY)
        bombY += bombY_change

    collision = iscollision(mostrX,mostrY,bombX,bombY)
    if collision:
        bombY = 59
        bomb_state = "ready"
        score_value += 1
        mostrX = random.randint(0,750)
        mostrY = random.randint(350,550)
    score(x9,y9)
    pygame.display.update()
pygame.quit()
