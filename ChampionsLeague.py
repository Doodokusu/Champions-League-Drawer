import pygame
import sys
import random
import time

groupLimit = 4
potLimit = 8

black = (0, 0, 0)
clBlue = (0, 51, 153)
groupColor = (0, 35, 135)

width = 1000
height = 600

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CL Groups")

class Team:
    def __init__(self, name, nation, pot):
        self.name = name
        self.nation = nation
        self.pot = pot

    isPlaced = False

    def getAvailableGroups(self, groups):
        availableGroups = []
        for i in range(len(groups)):
            isAvailable = True
            for m in range(len(groups[i])):
                if self.nation == groups[i][m].nation or self.pot == groups[i][m].pot:
                    isAvailable = False
            if isAvailable:
                availableGroups.append(groups[i])
        return availableGroups
    
groups = []
pots = []

teams = [
    Team("Man City", "eng", 1),
    Team("Sevilla", "spa", 1),
    Team("Barcelona", "spa", 1),
    Team("Napoli", "ita", 1),
    Team("Bayern", "ger", 1),
    Team("PSG", "fra", 1),
    Team("Benfica", "por", 1),
    Team("Feyenoord", "ned", 1),
    Team("Real Madird", "spa", 2),
    Team("Man United", "eng", 2),
    Team("Inter", "ita", 2),
    Team("Bor. Dortmund", "ger", 2),
    Team("Atl. Madrid", "spa", 2),
    Team("Leipzig", "ger", 2),
    Team("Porto", "por", 2),
    Team("Arsenal", "eng", 2),
    Team("Shakhtar", "ukr", 3),
    Team("Salzburg", "aus", 3),
    Team("Copenhagen", "den", 3),
    Team("PSV", "ned", 3),
    Team("Milan", "ita", 3),
    Team("Braga", "por", 3),
    Team("Lazio", "ita", 3),
    Team("Crvena Zvedza", "ser", 3),
    Team("Antwerp", "bel", 4),
    Team("Young Boys", "swi", 4),
    Team("Sociedad", "spa", 4),
    Team("Galatasaray", "tur", 4),
    Team("Celtic", "sco", 4),
    Team("Newcastle", "eng", 4),
    Team("Union Berlin", "ger", 4),
    Team("Lens", "fra", 4)
]

for i in range(int(len(teams)/groupLimit)):
    groups.append([])

for i in range(int(len(teams)/potLimit)):
    pots.append([])

for i in range(len(teams)):
    pots[teams[i].pot-1].append(teams[i])

for k in range(len(pots)):
    for i in range(len(pots[k])):
        availableGroups = pots[k][i].getAvailableGroups(groups)
        if len(availableGroups) == 1:
            availableGroups[0].append(pots[k][i])
    for j in range(len(pots[k])):
        availableTeams = []
        if pots[k][j].isPlaced:
            pass
        else:
            availableTeams.append(pots[k][j])
            randomTeam = random.choice(availableTeams)
            availableGroups = randomTeam.getAvailableGroups(groups)
            randomGroup = random.choice(availableGroups)
            randomGroup.append(randomTeam)

def drawText(text, font, x, y):
    text1 = font.render(text, 1, black)
    textRect = text1.get_rect(topleft=(x, y))
    screen.blit(text1, textRect)

def main():
    font = pygame.font.Font(None, 36)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(clBlue)
        x = 30
        y = 30
        for i in range(8):
            pygame.draw.rect(screen, groupColor, (x, y, 220, 220))
            x += 240
            if i == 3:
                x = 30
                y += 300

        x = 50
        y = 50
        numberOfGroups = 0
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