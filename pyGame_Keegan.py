import pygame as pygame
import sys
import random as random

def moveBall():
    global white, location, radius, thickness, black, screenSize, speedx, speedy, ballRect, deadBall, playerAScore, playerBScore, padA, padB

    if location[0] + radius >= screenSize[0]:
        playerAScore = playerAScore + 1
        victoryCheck()
        deadBall = True
        reset()
    elif location[0] - radius <= 0:
        playerBScore = playerBScore + 1
        victoryCheck()
        deadBall = True
        reset()

    if location[1] + radius >= screenSize[1] or location[1] - radius <= 0:
        speedy = -speedy

   
   
   
    location[0] = location[0] + speedx
    ballRect = ballRect.move(speedx, 0)
    location[1] = location[1] + speedy
    ballRect = ballRect.move(0, speedy)

    if collide(ballRect, padA) or collide(ballRect, padB):
        speedx = -speedx
        speedy = -speedy

    pygame.draw.circle(window, red, location, radius, thickness)
    

def drawVictory(text):
    global victory
    victory = True
    textC = font.render(text, True, black)
    window.blit(textC, (0, screenSize[1]//2))

def clearVictory():
    global text
    text = ""

def movePaddle():
    global blue, padA, screenSize, aSpeed, padB, bSpeed, padA2, padB2, a2Speed, b2Speed
    if padA.bottom >= screenSize[1] and aSpeed > 0:
        aSpeed = 0
    if padA.top <= 0 and aSpeed <0:
        aSpeed = 0
    padA = padA.move(0, aSpeed)
    pygame.draw.rect(window, blue, padA)
    
    if padA2.bottom >= screenSize[1] and a2Speed > 0:
        a2Speed = 0
    if padA2.top <= 0 and a2Speed <0:
        a2Speed = 0
    padA2 = padA2.move(0, a2Speed)
    pygame.draw.rect(window, blue, padA2)

    if padB.bottom >= screenSize[1] and bSpeed > 0:
        bSpeed = 0
    if padB.top <= 0 and bSpeed <0:
        bSpeed = 0
    padB = padB.move(0, bSpeed)
    pygame.draw.rect(window, blue, padB)
    
    if padB2.bottom >= screenSize[1] and b2Speed > 0:
        b2Speed = 0
    if padB2.top <= 0 and b2Speed <0:
        b2Speed = 0
    padB2 = padB2.move(0, b2Speed)
    pygame.draw.rect(window, blue, padB2)


def collide(rect1, rect2):
    if (rect1.colliderect(rect2)):
        return True
    else:
        return False

def displayScore():
    global font, playerAScore, playerBScore, white, screenSize
    
    textA = font.render(str(playerAScore), True, white)
    textB = font.render(str(playerBScore), True, white)
    window.blit(textA, (screenSize[0]//4, 30))
    window.blit(textB, (3*screenSize[0]//4, 30))

def reset():
    global screenSize, speedx, speedy, location, deadBall, text
    location[0] = screenSize[0]//2
    location[1] = screenSize[1]//2
    ballRect.center = (screenSize[0]//2, screenSize[1]//2)
    speedx = 0
    speedy = 0
    deadBall = True
    

def serve():
    global speedx, speedy
    
    speedx = random.randrange(-3, 3, 1)
    if speedx == 0:
        speedx = -2
    speedy = random.randrange(-3, 3, 1)
    deadBall = False

def victoryCheck():
    global playerAScore, playerBScore, font, black, screenSize, text
    if playerAScore >= 3 and playerAScore - 2 >= playerBScore:
        text = "Player 1 Wins! Press 'R' to Play Again"
        print("Player 1 Wins!")
        playerAScore = 0
        playerBScore = 0
    elif playerBScore >= 3 and playerBScore - 2 >= playerAScore:
        text = "Player 2 Wins! Press 'R' to Play Again"
        print("Player 2 Wins!")
        playerAScore = 0
        playerBScore = 0
        
    #reset()




speedx = 3
speedy = 3
screenSize = (1000, 750)
black = (0, 0, 0)
green = (90, 255, 0)
thickness = 0
red = (255, 0, 0)
orange = (255, 165, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
timer = pygame.time.Clock()
location = [450, 300]
radius = 20
padA = pygame.Rect((0, 325), (20, 100))
padB = pygame.Rect((980, 325), (20, 100))
padA2 = pygame.Rect((50, 325), (20, 100))
padB2 = pygame.Rect((910, 325), (20, 100))
ballRect= pygame.Rect((location[0]-radius, location[1]-radius), (radius *2, radius*2))
window = pygame.display.set_mode(screenSize)
fps = 60
text = ""
aSpeed = 0
a2Speed = 0
bSpeed = 0
b2Speed = 0
deadBall = False
playerAScore = 0
playerBScore = 0
font = pygame.font.init()
font = pygame.font.Font(None, 80)
yPos = 0




while True:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                aSpeed = -3
            elif event.key == pygame.K_s:
                aSpeed = 3
            elif event.key == pygame.K_r:
                a2Speed = -3
            elif event.key == pygame.K_f:
                a2Speed = 3
                
            elif event.key == pygame.K_UP:
                bSpeed = -3       
            elif event.key == pygame.K_DOWN:
                bSpeed = 3
            elif event.key == pygame.K_KP8:
                b2Speed = -3
            elif event.key == pygame.K_KP2:
                b2Speed = 3
                
            elif event.key == pygame.K_SPACE and deadBall == True:
                serve()
            elif event.key == pygame.K_r and victory == True:
                clearVictory()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                aSpeed= 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                bSpeed= 0
            elif event.key == pygame.K_r or event.key == pygame.K_f:
                a2Speed= 0
            elif event.key == pygame.K_KP8 or event.key == pygame.K_KP2:
                b2Speed= 0
            
        
    movePaddle()
    displayScore()
    drawVictory(text)
    moveBall()
    collide(ballRect, padA)
    collide(ballRect, padA2)
    collide(ballRect, padB)
    collide(ballRect, padB2)
    pygame.display.flip()
    window.fill(green)
    while yPos < screenSize[1]:
        pygame.draw.line(window, white,(screenSize[0]//2, yPos),(screenSize[0]//2, yPos + 40), 10)
        yPos = yPos + 50
    yPos = 0
    timer.tick(fps)