# import library
import pygame
import time
import random

# initialize pygame
pygame.init()

speed = 13
windowX = 720  # width of screen
windowY = 480  # height of screen

# forming colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

# setting title of current screen
pygame.display.set_caption("Snake Game --byTanviSharma")

# setting screen size
window = pygame.display.set_mode((windowX, windowY))

# default snake position and body
snakePosition = [100, 60]
snakeBody = [[100,60], [90,60], [80,60], [70,60]]

# generate random food position
def genrateRandomFoodPosition():
    # return [
    #     random.randrange(1, (windowX // 10) * 10),
    #     random.randrange(1, (windowY // 10) * 10)
    # ]
    while True:
        foodPosition = [
            random.randrange(1, (windowX // 10) * 10),
            random.randrange(1, (windowY // 10) * 10)
        ]
        if foodPosition not in snakeBody:
            return foodPosition

foodPosition = genrateRandomFoodPosition()

direction = "RIGHT"
score = 0

def showScore(choice, color, font, size):
    scoreFont = pygame.font.SysFont(font, size)  # styling the score font
    scoreSurface = scoreFont.render("SCORE: " + str(score), True, color) # surface containing the rendered text
    scoreRect = scoreSurface.get_rect() # gets the rectangular bounding box for the text that was rendered
    window.blit(scoreSurface, scoreRect) # displayed on the screen

def gameOver():
    font = pygame.font.SysFont("Roboto", 50)
    gameOverSurface = font.render("YOUR SCORE IS: " + str(score), True, BLUE)
    gameOverRect = gameOverSurface.get_rect()
    gameOverRect.midtop = (windowX / 2, windowY / 4)
    window.blit(gameOverSurface, gameOverRect)

    pygame.display.flip() # updating display
    time.sleep(2)         
    pygame.quit() # deactivate all libraries

    quit() # close the game

#frame per second controller
fps = pygame.time.Clock()

while True:
    # events handle
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direction != "DOWN": # can't directly move up from down direction
                    direction = "UP"
            if event.key == pygame.K_DOWN:
                if direction != "UP": # can't directly move down from up direction
                    direction = "DOWN" 
            if event.key == pygame.K_LEFT:
                if direction != "RIGHT": # can't directly move left from right direction
                    direction = "LEFT"
            if event.key == pygame.K_RIGHT:
                if direction != "LEFT": # can't directly move right from left direction
                    direction = "RIGHT"
        
    if direction == "UP":
        snakePosition[1] = snakePosition[1] - 10
    if direction == "DOWN":
        snakePosition[1] = snakePosition[1] + 10
    if direction == "LEFT":
        snakePosition[0] = snakePosition[0] - 10
    if direction == "RIGHT":
        snakePosition[0] = snakePosition[0] + 10
    
    # increasing the score and growing snake body on eating food
    snakeBody.insert(0, list(snakePosition))
    if snakePosition[0] == foodPosition[0] and snakePosition[1] == foodPosition[1] or pygame.Rect(foodPosition[0], foodPosition[1], 10, 10).collidepoint(snakePosition[0], snakePosition[1]):
        score = score + 10
        # changing food position after every bite
        foodPosition = genrateRandomFoodPosition()
    else:
        snakeBody.pop()

    window.fill(BLACK)

    for sb in snakeBody:
        pygame.draw.rect(window, RED, pygame.Rect(sb[0], sb[1],20,20))

    pygame.draw.rect(window, WHITE, pygame.Rect(foodPosition[0], foodPosition[1],20,20))

    # game over
    if snakePosition[0] < 0 or snakePosition[0] > windowX-10:
        gameOver()
    if snakePosition[1] < 0 or snakePosition[1] > windowY-10:
        gameOver()

    showScore(1,WHITE,"Robot", 20)

    # refresh game screen
    pygame.display.update()

    # smoothening the game
    fps.tick(speed)