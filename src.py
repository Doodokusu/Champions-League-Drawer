import random

#setting limits
groupLimit = 4
potLimit = 8

"""create a team class and a function that 
allows to find available groups of teams 
that do not have the same pot and country"""
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

#creating teams
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

#creating groups and adding to "groups" list
for i in range(int(len(teams)/groupLimit)):
    groups.append([])

#creating "pots" list
for i in range(int(len(teams)/potLimit)):
    pots.append([])

#adding teams to pots
for i in range(len(teams)):
    pots[teams[i].pot-1].append(teams[i])

#drawing teams randomly
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