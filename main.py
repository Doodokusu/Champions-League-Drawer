import pygame
import sys
from src import *

#setting colors
white = (250, 250, 250)
clBlue = (9, 20, 66)
groupColor = (14, 30, 91)

#setting width and height of screen
width = 1000
height = 600

#intializing and displaying the screen
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CL Groups")

#creating drawText function to drawing texts
def drawText(text, font, x, y):
    text1 = font.render(text, 1, white)
    textRect = text1.get_rect(topleft=(x, y))
    screen.blit(text1, textRect)

def main():
    font = pygame.font.Font(None, 36)
    while True:
        for event in pygame.event.get():        #enabling exit button
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(clBlue)                     #filling the screen blue 
        x = 30
        y = 30
        for i in range(8):                      #putting a square behing the groups to make them more distinct
            pygame.draw.rect(screen, groupColor, (x, y, 220, 220))
            x += 240
            if i == 3:
                x = 30
                y += 300

        x = 50
        y = 50
        numberOfGroups = 0
        #printing groups
        for group in range(len(groups)):
            drawText(f"{str(group+1)}. Group", font, x, y)
            y += 50
            for team in range(len(groups[group])):
                drawText(f"- {groups[group][team].name}", font, x, y)
                y += 30
            x += 240
            y -= 170
            if numberOfGroups == 3:
                y += 300
                x = 50
            numberOfGroups += 1

        pygame.display.flip()

main()