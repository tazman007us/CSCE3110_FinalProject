# The Wumpus World
# Robert Powell
# 5/07/2022

import os
import random

# Legend
legend = [['A', 'Agent'], ['B', 'Breeze'], ['G', 'Gold'], ['OK', 'Safety'],
          ['P', 'Pit'], ['S', 'Stench'], ['?', '!Visited'], ['W', 'Wumpus']]

wumpusMap = []

# wumpusMap1
wumpusMap1 = [[1, 2, 5, -1, -1, ' ', 'OK', '?', ' '],
             [2, 3, 6, 1, -1, ' ', 'OK', '?', 'S'],
             [3, 4, 7, 2, -1, ' ', '!OK', '?', 'W'],
             [4, -1, 8, 3, -1, ' ', 'OK', '?', 'S'],
             [5, 6, 9, -1, 1, ' ', 'OK', '?', 'B'],
             [6, 7, 10, 5, 2, ' ', 'OK', '?', ' '],
             [7, 8, 11, 6, 3, ' ', 'OK', '?', 'B,G,S'],
             [8, -1, 12, 7, 4, ' ', 'OK', '?', ' '],
             [9, 10, 13, -1, 5, ' ', '!OK', '?', 'P'],
             [10, 11, 14, 9, 6, ' ', 'OK', '?', 'B'],
             [11, 12, 15, 10, 7, ' ', '!OK', '?', 'P'],
             [12, -1, 16, 11, 8, ' ', 'OK', '?', 'B'],
             [13, 14, -1, -1, 9, ' ', 'OK', '?', 'B'],
             [14, 15, -1, 13, 10, ' ', 'OK', '?', ' '],
             [15, 16, -1, 14, 11, ' ', 'OK', '?', 'B'],
             [16, -1, -1, 15, 12, ' ', '!OK', '?', 'P'],
             ]

wumpusMap2 = [[1, 2, 5, -1, -1, ' ', 'OK', '?', ''],
             [2, 3, 6, 1, -1, ' ', 'OK', '?', ''],
             [3, 4, 7, 2, -1, ' ', 'OK', '?', 'B,S'],
             [4, -1, 8, 3, -1, ' ', '!OK', '?', 'P'],
             [5, 6, 9, -1, 1, ' ', 'OK', '?', 'B'],
             [6, 7, 10, 5, 2, ' ', 'OK', '?', 'S'],
             [7, 8, 11, 6, 3, ' ', '!OK', '?', 'W'],
             [8, -1, 12, 7, 4, ' ', 'OK', '?', 'B,S'],
             [9, 10, 13, -1, 5, ' ', '!OK', '?', 'P'],
             [10, 11, 14, 9, 6, ' ', 'OK', '?', 'B,G'],
             [11, 12, 15, 10, 7, ' ', 'OK', '?', 'B,S'],
             [12, -1, 16, 11, 8, ' ', '!OK', '?', 'P'],
             [13, 14, -1, -1, 9, ' ', 'OK', '?', 'B'],
             [14, 15, -1, 13, 10, ' ', 'OK', '?', ''],
             [15, 16, -1, 14, 11, ' ', 'OK', '?', ''],
             [16, -1, -1, 15, 12, ' ', 'OK', '?', 'B'],
             ]

wumpusMap3 = [[1, 2, 5, -1, -1, ' ', 'OK', '?', 'B'],
             [2, 3, 6, 1, -1, ' ', 'OK', '?', ''],
             [3, 4, 7, 2, -1, ' ', 'OK', '?', 'B'],
             [4, -1, 8, 3, -1, ' ', 'OK', '?', ''],
             [5, 6, 9, -1, 1, ' ', '!OK', '?', 'P'],
             [6, 7, 10, 5, 2, ' ', 'OK', '?', 'B'],
             [7, 8, 11, 6, 3, ' ', '!OK', '?', 'P'],
             [8, -1, 12, 7, 4, ' ', 'OK', '?', 'B'],
             [9, 10, 13, -1, 5, ' ', 'OK', '?', 'B,S'],
             [10, 11, 14, 9, 6, ' ', '!OK', '?', 'W'],
             [11, 12, 15, 10, 7, ' ', 'OK', '?', 'B,S'],
             [12, -1, 16, 11, 8, ' ', 'OK', '?', 'G'],
             [13, 14, -1, -1, 9, ' ', 'OK', '?', ''],
             [14, 15, -1, 13, 10, ' ', 'OK', '?', 'B,S'],
             [15, 16, -1, 14, 11, ' ', '!OK', '?', 'P'],
             [16, -1, -1, 15, 12, ' ', 'OK', '?', 'B'],
             ]


# displayed message
mapMessage = ['','','','','']   # sets initial map message to empty string


# Game attributes
playerRotation = [0]        # set initial rotation value to zero
playerPosition = [0]        # set initial position value to zero
playerColumn = [0]          # column player is in
playerRow = [0]             # row player is in    
playerScore = [0]           # Number of points in game - current value
playerArrows = [0]          # Number of arrows in game - current value
nextPlayerPosition = [0]    # room after moving forward by one
wumpusDead = [0]            # 1 if player slayed the Wumpus
wumpusRoom = [0]            # room number that Wumpus lives
wumpusColumn = [0]          # column of Wumpus room
wumpusRow = [0]             # row of Wumpus room
playerLife = [1]            # 1 if player is alive, 0 if dead
playerHasGold = [0]         # 1 if player has gold, 0 if not
playerMoveCount = [0]       # keeps track of how many moves taken rotate + move forward
playerSurvival = [1]        # 1 if player survives, 0 if death occurs
playerWon = [0]             # initial win state 0, set to 1 if player wins.
playerLost = [0]            # initial lose state 0, set to 1 if player loses.
playerClimb = [0]           # initial state 0, set to 1 after player climbs
mapNumber = [0]             # map number


#generate a random number to load the appropriate map
mapNumber[0] = random.choice([1, 2, 3])

#mapNumber[0] = 3

if mapNumber[0] == 1:
    wumpusMap = wumpusMap1
elif mapNumber[0] == 2:
    wumpusMap = wumpusMap2
elif mapNumber[0] == 3:
    wumpusMap = wumpusMap3




def printLegend(legMessage, legItem):
    leg1A = legend[0][legItem]
    leg2A = legend[1][legItem]
    leg3A = legend[2][legItem]
    leg4A = legend[3][legItem]
    leg5A = legend[4][legItem]
    leg6A = legend[5][legItem]
    leg7A = legend[6][legItem]
    leg8A = legend[7][legItem]
    leg1B = legend[0][legItem - 1]
    leg2B = legend[1][legItem - 1]
    leg3B = legend[2][legItem - 1]
    leg4B = legend[3][legItem - 1]
    leg5B = legend[4][legItem - 1]
    leg6B = legend[5][legItem - 1]
    leg7B = legend[6][legItem - 1]
    leg8B = legend[7][legItem - 1]

    print('\n')
    print(legMessage)
    print('---------------------------------------------------------------------------------')
    print('|{:^9}|{:^9}|{:^9}|{:^9}|{:^9}|{:^9}|{:^9}|{:^9}|'.format(leg1A, leg2A, leg3A, leg4A,
                                                                     leg5A, leg6A, leg7A, leg8A))
    print('---------------------------------------------------------------------------------')
    print('|{:^9}|{:^9}|{:^9}|{:^9}|{:^9}|{:^9}|{:^9}|{:^9}|'.format(leg1B, leg2B, leg3B, leg4B,
                                                                     leg5B, leg6B, leg7B, leg8B))
    print('---------------------------------------------------------------------------------')


def drawMap(mapMessage, roomItem):
    room1 = wumpusMap[0][roomItem]
    room2 = wumpusMap[1][roomItem]
    room3 = wumpusMap[2][roomItem]
    room4 = wumpusMap[3][roomItem]
    room5 = wumpusMap[4][roomItem]
    room6 = wumpusMap[5][roomItem]
    room7 = wumpusMap[6][roomItem]
    room8 = wumpusMap[7][roomItem]
    room9 = wumpusMap[8][roomItem]
    room10 = wumpusMap[9][roomItem]
    room11 = wumpusMap[10][roomItem]
    room12 = wumpusMap[11][roomItem]
    room13 = wumpusMap[12][roomItem]
    room14 = wumpusMap[13][roomItem]
    room15 = wumpusMap[14][roomItem]
    room16 = wumpusMap[15][roomItem]

    print("\n")
    print("%s" % mapMessage[0])
    print("%s" % mapMessage[1])
    print("%s" % mapMessage[2])
    print("%s" % mapMessage[3])
    print("%s" % mapMessage[4])
    print('#########################################')
    print('#{:^9}#{:^9}#{:^9}#{:^9}#'.format(room4, room8, room12, room16) + "             Score: " + '{:^9}'.format(playerScore[0]))
    print('#########################################')
    print('#{:^9}#{:^9}#{:^9}#{:^9}#'.format(room3, room7, room11, room15) + "             Arrow: " + '{:^9}'.format(playerArrows[0]))
    print('#########################################')
    print('#{:^9}#{:^9}#{:^9}#{:^9}#'.format(room2, room6, room10, room14))
    print('#########################################')
    print('#{:^9}#{:^9}#{:^9}#{:^9}#'.format(room1, room5, room9, room13))
    print('#########################################')


# playerRotation = 0

def rotateLeft():
    playerMoveCount[0] = playerMoveCount[0] + 1 # add one to move count
    if playerRotation[0] == 62:
        playerRotation[0] = 94
    elif playerRotation[0] == 94:
        playerRotation[0] = 60
    elif playerRotation[0] == 60:
        playerRotation[0] = 118
    elif playerRotation[0] == 118:
        playerRotation[0] = 62


def rotateRight():
    playerMoveCount[0] = playerMoveCount[0] + 1 # add one to move count
    if playerRotation[0] == 62:
        playerRotation[0] = 118
    elif playerRotation[0] == 118:
        playerRotation[0] = 60
    elif playerRotation[0] == 60:
        playerRotation[0] = 94
    elif playerRotation[0] == 94:
        playerRotation[0] = 62


def getPlayerRotation():
    return playerRotation[0]


def getPlayerPosition(): # set player row and column position as well as return player current room
    if playerPosition[0] == 1 or playerPosition[0] == 2 or playerPosition[0] == 3 or playerPosition[0] == 4: # find column 1
        playerColumn[0] = 1
    if playerPosition[0] == 5 or playerPosition[0] == 6 or playerPosition[0] == 7 or playerPosition[0] == 8: # find column 2
        playerColumn[0] = 2
    if playerPosition[0] == 9 or playerPosition[0] == 10 or playerPosition[0] == 11 or playerPosition[0] == 12: # find column 3
        playerColumn[0] = 3
    if playerPosition[0] == 13 or playerPosition[0] == 14 or playerPosition[0] == 15 or playerPosition[0] == 16: # find column 4
        playerColumn[0] = 4
    if playerPosition[0] == 1 or playerPosition[0] == 5 or playerPosition[0] == 9 or playerPosition[0] == 13: # find row 1
        playerRow[0] = 1
    if playerPosition[0] == 2 or playerPosition[0] == 6 or playerPosition[0] == 10 or playerPosition[0] == 14: # find row 2
        playerRow[0] = 2
    if playerPosition[0] == 3 or playerPosition[0] == 7 or playerPosition[0] == 11 or playerPosition[0] == 15: # find row 3
        playerRow[0] = 3
    if playerPosition[0] == 4 or playerPosition[0] == 8 or playerPosition[0] == 12 or playerPosition[0] == 16: # find row 4
        playerRow[0] = 4
    return playerPosition[0]


def getPlayerScore():
    return playerScore[0]


def getPlayerArrows():
    return playerArrows[0]


def checkNextroom():
    if wumpusMap[nextPlayerPosition[0]-1][-1] == 'B':
        breezeMessage()
        playerSurvival[0] = 1
    elif wumpusMap[nextPlayerPosition[0]-1][-1] == 'B,S':
        breezeMessage()
        theWumpusSmellMessage()
        playerSurvival[0] = 1
    elif wumpusMap[nextPlayerPosition[0]-1][-1] == 'S':
        theWumpusSmellMessage()
        playerSurvival[0] = 1
    elif wumpusMap[nextPlayerPosition[0]-1][-1] == 'B,G,S' or wumpusMap[nextPlayerPosition[0]-1][-1] == 'B,G' or wumpusMap[nextPlayerPosition[0]-1][-1] == 'G,S' or wumpusMap[nextPlayerPosition[0]-1][-1] == 'G':
        goldRoomMessage()
        playerSurvival[0] = 1
    elif wumpusMap[nextPlayerPosition[0]-1][-1] == 'P':
        pitDeathMessage()
        ripDeathMessage()
        playerSurvival[0] = 0
    elif wumpusMap[nextPlayerPosition[0]-1][-1] == 'W':
        if wumpusDead[0] == 1:
            deadWumpusRoomMessage()
            playerSurvival[0] = 1
        elif wumpusDead[0] == 0:
            theWumpusDeathMessage()
            ripDeathMessage()
            playerSurvival[0] = 0
        
    return playerSurvival[0]       
  
# if player survives move forward then remove tracks
# if play finds death room end game

def moveForward():
    mapMessage[0] = "" # reset message
    mapMessage[1] = "" # reset message
    mapMessage[2] = "" # reset message    
    if getNextPlayerPosition() == -1:
        wallTryAgainMessage()
        playerScore[0] = playerScore[0] - 5  # -5 for hitting wall
    elif checkNextroom() == 0: # player dies
        playerMoveCount[0] = playerMoveCount[0] + 1 # add one to move count
        temp = playerPosition[0]
        playerPosition[0] = getNextPlayerPosition()   # sets the player position in map
        wumpusMap[temp-1][-2] = wumpusMap[temp-1][-1] # display the discovered room contents
        # wumpusMap[temp-1][-2] = chr(32)  # erase previous player position - for later installation of hard mode
        playerScore[0] = playerScore[0] - 1000  # death penalty
        mapMessage[2] = "You Lost ..."
        playerLost[0] = 1 

    elif checkNextroom() == 1: # player survives
        playerMoveCount[0] = playerMoveCount[0] + 1 # add one to move count
        temp = playerPosition[0]
        playerPosition[0] = getNextPlayerPosition()   # sets the player position in map
        wumpusMap[temp-1][-2] = wumpusMap[temp-1][-1] # display the discovered room contents
        playerScore[0] = playerScore[0] - 1  # minus one for movement
        if ((playerPosition[0] == 1) and (playerHasGold[0] == 1)):
                playerScore[0] = playerScore[0] + 1000
                mapMessage[2] = "You Won!!!"
                playerWon[0] = 1    
    

# find next position

def getNextPlayerPosition():
    getPlayerRotation()
    if playerRotation[0] == 94:  # up
        nextPlayerPosition[0] = wumpusMap[getPlayerPosition() - 1][1]
    elif playerRotation[0] == 62:  # right
        nextPlayerPosition[0] = wumpusMap[getPlayerPosition() - 1][2]
    elif playerRotation[0] == 118:  # down
        nextPlayerPosition[0] = wumpusMap[getPlayerPosition() - 1][3]
    elif playerRotation[0] == 60:  # left
        nextPlayerPosition[0] = wumpusMap[getPlayerPosition() - 1][4]
    
    return nextPlayerPosition[0]        

# find wumpusRoom
def findWumpusRoom():
    count = 0
    while count < 16:
        if wumpusMap[count][-1] == 'W':
            wumpusRoom[0] = count + 1
            count = 16
        else:
            count = count + 1

    if wumpusRoom[0] == 1 or wumpusRoom[0] == 2 or wumpusRoom[0] == 3 or wumpusRoom[0] == 4: # find column 1
        wumpusColumn[0] = 1
    if wumpusRoom[0] == 5 or wumpusRoom[0] == 6 or wumpusRoom[0] == 7 or wumpusRoom[0] == 8: # find column 2
        wumpusColumn[0] = 2
    if wumpusRoom[0] == 9 or wumpusRoom[0] == 10 or wumpusRoom[0] == 11 or wumpusRoom[0] == 12: # find column 3
        wumpusColumn[0] = 3
    if wumpusRoom[0] == 13 or wumpusRoom[0] == 14 or wumpusRoom[0] == 15 or wumpusRoom[0] == 16: # find column 4
        wumpusColumn[0] = 4
    if wumpusRoom[0] == 1 or wumpusRoom[0] == 5 or wumpusRoom[0] == 9 or wumpusRoom[0] == 13: # find row 1
        wumpusRow[0] = 1
    if wumpusRoom[0] == 2 or wumpusRoom[0] == 6 or wumpusRoom[0] == 10 or wumpusRoom[0] == 14: # find row 2
        wumpusRow[0] = 2
    if wumpusRoom[0] == 3 or wumpusRoom[0] == 7 or wumpusRoom[0] == 11 or wumpusRoom[0] == 15: # find row 3
        wumpusRow[0] = 3
    if wumpusRoom[0] == 4 or wumpusRoom[0] == 8 or wumpusRoom[0] == 12 or wumpusRoom[0] == 16: # find row 4
        wumpusRow[0] = 4



# hit wall message
def wallTryAgainMessage():
    select = playerMoveCount[0] % 10
    if select == 0:    
        mapMessage[0] = "Wall faceplant.  Try again."
    elif select == 1:       
        mapMessage[0] = "Oh no.  You hit a wall.  Try again."
    elif select == 2:
        mapMessage[0] = "Bump.  Try again."
    elif select == 3:
        mapMessage[0] = "Cannot go that way.  Try again."
    elif select == 4:
        mapMessage[0] = "Dead End.  Try again."
    elif select == 5:
        mapMessage[0] = "Nope.  Try again."
    elif select == 6:
        mapMessage[0] = "No Way Through.  Try again."
    elif select == 7:
        mapMessage[0] = "Can't you read the sign?  Try again."
    elif select == 8:
        mapMessage[0] = "Stopped in your tracks.  Try again."
    elif select == 9:
        mapMessage[0] = "Thou Shall Not Pass.  Try again."


# found treasure message

def goldRoomMessage():
    select = playerMoveCount[0] % 10
    if select == 0:    
        mapMessage[0] = "Wait ... Gold, a breeze, and a bad smell"
        mapMessage[1] = "Get me outa here. (After picking up the gold)."
    elif select == 1:
        mapMessage[0] = "Found the Gold, it is cold and smells bad"
        mapMessage[1] = "Get me outa here. (After picking up the gold)."
    elif select == 2:
        mapMessage[0] = "Gold, Gold, Gold"
        mapMessage[1] = "Bad smell and its cold. Pickup the gold and go."
    elif select == 3:
        mapMessage[0] = "Why does the Gold have to bed in stinky breezy room."
        mapMessage[1] = "Get me outa here. (After picking up the gold)."
    elif select == 4:    
        mapMessage[0] = "Gold, Oh Yeah. Smell Bad. Oh Yeah. And Breezy"
        mapMessage[1] = "Oh Yeah.  Pick Gold and go.  Oh Yeah."
    elif select == 5:
        mapMessage[0] = "Smelly Gold, Oh Smelly Gold"
        mapMessage[1] = "Cold and Breezy, and Let's get Outa Here."
    elif select == 6:
        mapMessage[0] = "What could be better than finding Gold?"
        mapMessage[1] = "Maybe if it wasn't in a breezy stinky room!!!"
    elif select == 7:
        mapMessage[0] = "Smells like smeltering some gold we have here."
        mapMessage[1] = "Cold and breezy also. Let's Gooooooo!!!"
    elif select == 8:
        mapMessage[0] = "Gold, Gold, and Smelly Gold.  And breezy too."
        mapMessage[1] = "Get me outa here. (After picking up the gold)."    
    elif select == 9:
        mapMessage[0] = "Wait ... Gold, a breeze, and a bad smell"
        mapMessage[1] = "Get me outa here. (After picking up the gold)."


# found kill message

def deadWumpusRoomMessage():
    select = playerMoveCount[0] % 10
    if select == 0:
        mapMessage[0] = "A cold dead corpse lay on the floor."
        mapMessage[1] = "The arrow slayed the Wumpus"
    elif select == 1:
        mapMessage[0] = "A cold dead corpse lay on the floor."
        mapMessage[1] = "The Wumpus is No More."
    elif select == 2:
        mapMessage[0] = "You Did It."
        mapMessage[1] = "the Wumpus Is Dead."
    elif select == 3:
        mapMessage[0] = "Kill the Rabbit, Kill the Rabbit."
        mapMessage[1] = "I mean Kill the Wumpus you did."
    elif select == 4:    
        mapMessage[0] = "Wumpus."
        mapMessage[1] = "No More."
    elif select == 5:
        mapMessage[0] = "He stares at you with cold dark eyes."
        mapMessage[1] = "Its almost sad seeing the slain Wumpus this way."
    elif select == 6:
        mapMessage[0] = "A cold dead corpse lay on the floor."
        mapMessage[1] = "The arrow slayed the Wumpus"
    elif select == 7:
        mapMessage[0] = "The Wumpus is Gone."
        mapMessage[1] = "Just his Furry Lifeless Corpse Remains."
    elif select == 8:
        mapMessage[0] = "The Wumpus is Dead."
        mapMessage[1] = "The Wumpus is Dead."
    elif select == 9:
        mapMessage[0] = "Even Lifeless as he is."
        mapMessage[1] = "The Wumpus Looks Scary Still."

# danger near messages

def breezeMessage():
    select = playerMoveCount[0] % 10
    if select == 0:
        mapMessage[3] = "Blow, blow, thou winter wind, ..."
        mapMessage[4] = "Someone named Shakespeare said that."
    elif select == 1:
        mapMessage[3] = "Wait ... Wait ... a breeze ..."
        mapMessage[4] = "But where does it come from?"
    elif select == 2:
        mapMessage[3] = "Somebody give me a blanket"
        mapMessage[4] = "I feel such a cold draft"
    elif select == 3:
        mapMessage[3] = "Feels a bit drafty"
        mapMessage[4] = "Guess one should watch their step"
    elif select == 4:
        mapMessage[3] = "Feels a bit drafty"
        mapMessage[4] = "Mind the Gap"
    elif select == 5:
        mapMessage[3] = "Feels a bit drafty"
        mapMessage[4] = "Guess one should watch their step"
    elif select == 6:
        mapMessage[3] = "Feels a bit drafty"
        mapMessage[4] = "Guess one should watch their step"
    elif select == 7:
        mapMessage[3] = "Feels a bit drafty"
        mapMessage[4] = "Guess one should watch their step"
    elif select == 8:
        mapMessage[3] = "Feels a bit drafty"
        mapMessage[4] = "Guess one should watch their step"
    elif select == 9:
        mapMessage[3] = "Feels a bit drafty"
        mapMessage[4] = "Guess one should watch their step"

def theWumpusSmellMessage():
    select = playerMoveCount[0] % 10
    if select == 0:
        mapMessage[0] = "fe fi fo fum i smell the blood of a Wumpus"
        mapMessage[1] = "The eyes water from such a stench"
    elif select == 1:    
        mapMessage[0] = "Wumpus"    
        mapMessage[1] = "The smell"
    elif select == 2:    
        mapMessage[0] = "Wumpus.  What's a Wumpus?"
        mapMessage[1] = "If the smell is any indication, we don't want to find out."
    elif select == 3:    
        mapMessage[0] = "Ooooh that smell. Can't you smell that smell"
        mapMessage[1] = "Ooooh that smell. The smell of death surrounds you"
    elif select == 4:
        mapMessage[0] = "Somebody Needs a Bath"
        mapMessage[1] = "Must Be the Wumpus"
    elif select == 5:
        mapMessage[0] = "Oh No the Smell"
        mapMessage[1] = "Eyes Water. Can't Take It.'"
    elif select == 6:
        mapMessage[0] = "How Often Do Wumpeses Go to The Dentist?"
        mapMessage[1] = "From That Smell I Smell, Not too often."
    elif select == 7:
        mapMessage[0] = "WUMPUS!!!"
        mapMessage[1] = "Don't think even Old Spice would help you."
    elif select == 8:
        mapMessage[0] = "What smells worse than a Wumpus?"
        mapMessage[1] = "You thought I was going to tell you? I don't have a clue."    
    elif select == 9:
        mapMessage[0] = "Smelly Cat, Oh Smelly Cat. ... Wrong Song."
        mapMessage[1] = "Been a while sense the show FRIENDS.  Smells like a Wumpus is near."        


# Death Messages   

def theWumpusDeathMessage():
    select = playerMoveCount[0] % 10
    if select == 0:
        mapMessage[0] = "Mr. Wumpus - Hugged you until you could not breath and would not let go."
    elif select == 1:
        mapMessage[0] = "Mr. Wumpus - Was so glad to see you, he flung you around in joy until your limbs fell off."
    elif select == 2:
        mapMessage[0] = "Mr. Wumpus - Just wanted to go home.  Problem was, you were in his way."
    elif select == 3:
        mapMessage[0] = "Mr. Wumpus - Picked you up so high you could not see the ground."
    elif select == 4:
        mapMessage[0] = "Mr. Wumpus - Just Wanted to PLAY"
    elif select == 5:
        mapMessage[0] = "Mr. Wumpus - Made You Snap Crackle Pop"
    elif select == 6:
        mapMessage[0] = "Mr. Wumpus - Made A Mess"
    elif select == 7:
        mapMessage[0] = "Mr. Wumpus - Does What Wumpuses Do"
    elif select == 8:
        mapMessage[0] = "Mr. Wumpus - Was Smiled At You"
    elif select == 9:
        mapMessage[0] = "Mr. Wumpus - Really was more scared than you." 


def pitDeathMessage():
    select = playerMoveCount[0] % 10
    if select == 0:
        mapMessage[0] = "You fell into the pit of despair"
    elif select == 1:    
        mapMessage[0] = "Suddenly you feel weightless.  And then ... After a long time, it all goes dark."
    elif select == 2:    
        mapMessage[0] = "Noooooooooooooooooooooooooo!!!"
    elif select == 3:
        mapMessage[0] = "The Lights Went Out In Georgia!!!"
    elif select == 4:    
        mapMessage[0] = "Mommy!!!"
    elif select == 5:    
        mapMessage[0] = "Suddenly you feel weightless.  And then ... After a long time, it all goes dark."
    elif select == 6:    
        mapMessage[0] = "Only One Breath"
    elif select == 7:
        mapMessage[0] = "Why Is It So Dark?"
    elif select == 8:
        mapMessage[0] = "Broken Garlic"
    elif select == 9:
        mapMessage[0] = "Going to Sell Salt"


def ripDeathMessage():
    select = playerMoveCount[0] % 10   
    if select == 0: 
        mapMessage[1] = "YOU DIED  _/¯(0 _ 0)¯\_  R.I.P."
    elif select == 1:    
        mapMessage[1] = "YOU DIED  _/¯(0 | 0)¯\_  R.I.P."
    elif select == 2:        
        mapMessage[1] = "YOU DIED  :(  R.I.P."
    elif select == 3:
        mapMessage[1] = "YOU DIED  ;|  R.I.P"
    elif select == 4:
        mapMessage[1] = "YOU DIED  =|  R.I.P."
    elif select == 5:
        mapMessage[1] = "YOU DIED  ¯\_(\")_/¯  R.I.P.  "
    elif select == 6:
        mapMessage[1] = "YOU DIED  [{  R.I.P"
    elif select == 7:
        mapMessage[1] = "YOU DIED  :)  R.I.P"
    elif select == 8:
        mapMessage[1] = "YOU DIED  :o)  R.I.P."
    elif select == 9:
        mapMessage[1] = "YOU DIED  :)~  R.I.P"
    

def pickupGold():
    if wumpusMap[getPlayerPosition() - 1][-1] == 'B,G,S' or wumpusMap[nextPlayerPosition[0]-1][-1] == 'B,G' or wumpusMap[nextPlayerPosition[0]-1][-1] == 'G,S' or wumpusMap[nextPlayerPosition[0]-1][-1] == 'G,S':
        mapMessage[0] = "Gold Picked Up."
        mapMessage[1] = "Can we find the exit please?"
        mapMessage[2] = ""
        return 1
    else:
        mapMessage[0] = "Nothing here."
        mapMessage[1] = "No Gold to Pickup."
        mapMessage[2] = ""        
        return 0

def shootArrow():
        if getPlayerRotation() ==94 and playerColumn[0]==wumpusColumn[0] and playerPosition[0] < wumpusRoom[0]: # ^ up
            mapMessage[0] = "A loud scream fills the halls."
            mapMessage[1] = "You killed Wumpus!!!"
            wumpusDead[0] = 1
            playerScore[0] = playerScore[0] - 10  # -10 for shooting arrow
            playerArrows[0] = 0
        elif getPlayerRotation() ==60 and playerRow[0]==wumpusRow[0] and playerPosition[0] > wumpusRoom[0]: # < left
            mapMessage[0] = "A horrible sound chills your spine."
            mapMessage[1] = "The Wumpus has fallen!!!"
            wumpusDead[0] = 1
            playerScore[0] = playerScore[0] - 10  # -10 for shooting arrow
            playerArrows[0] = 0
        elif getPlayerRotation() ==62 and playerRow[0]==wumpusRow[0] and playerPosition[0] < wumpusRoom[0]: # < right
            mapMessage[0] = "A horrible sound chills your spine."
            mapMessage[1] = "The Wumpus has fallen!!!"
            wumpusDead[0] = 1
            playerScore[0] = playerScore[0] - 10  # -10 for shooting arrow
            playerArrows[0] = 0
        elif getPlayerRotation() ==118 and playerColumn[0]==wumpusColumn[0] and playerPosition[0] > wumpusRoom[0]: # V down
            mapMessage[0] = "The shrill is so loud."
            mapMessage[1] = "The Wumpus screams, then falls with a thud."
            wumpusDead[0] = 1
            playerScore[0] = playerScore[0] - 10  # -10 for shooting arrow
            playerArrows[0] = 0
        else:
            mapMessage[0] = "Silence."
            mapMessage[1] = "Nothing but Silence."
            playerScore[0] = playerScore[0] - 10  # -10 for shooting arrow
            playerArrows[0] = 0



# start

os.system('cls')  # clear screen for cmd for Windows OS
os.system('clear')  # clear screen for cmd for Linux OS

legItem = -1
legMessage = "Wumpus World Legend (not Legend of Zelda)"
printLegend(legMessage, legItem)

mapMessage[0] = "Starting Point"
roomItem = -2
drawMap(mapMessage, roomItem)

findWumpusRoom() #finds the wumpusRoom and assigns row, column to Wumpus - used for shoot arrow

print('current map#: ' + str(mapNumber[0]))

menu_options = {
    1: 'Show Current Map State',
    2: 'Climb Up (only from first position)',
    3: 'Turn Left',
    4: 'Turn Right',
    5: 'Move Forward',
    6: 'Shoot Arrow',
    7: 'Grab Gold',
    8: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

def option1():
    # print('Handle option \'Option 1\'')
    # print('Show Current Map State \'Option 1\'')
    os.system('cls')    # clear screen for cmd for Windows OS
    os.system('clear')  # clear screen for cmd for Linux OS
    legItem = -1
    legMessage = "Wumpus World Legend (not Legend of Zelda)"
    printLegend(legMessage, legItem)
    roomItem = -2
    drawMap(mapMessage, roomItem)

def option2():
    if playerClimb[0] == 0:
        getPlayerPosition()
        mapMessage[0] = ""
        mapMessage[1] = ""
        mapMessage[2] = ""
        mapMessage[3] = ""
        mapMessage[4] = ""
        # print('Handle option \'Option 2\'')
        # print('Climb Up \'Option 2\'')
        _ascii = 62
        playerPosition[0] = 1
        playerArrows[0] = 1
        wumpusMap[playerPosition[0]-1][-2] = chr(_ascii)  # sets the player rotation in map
        playerRotation[0] = 62
        os.system('cls')  # clear screen for cmd for Windows OS
        os.system('clear')  # clear screen for cmd for Linux OS
        legItem = -1
        legMessage = "Wumpus World Legend (not Legend of Zelda)"
        printLegend(legMessage, legItem)
        roomItem = -2
        playerClimb[0] = 1

        if wumpusMap[getPlayerPosition()-1][-1] == 'B':
            breezeMessage()

        mapMessage[0] = "Climbing Up ..."
        drawMap(mapMessage, roomItem)
    elif playerClimb[0] == 1:
        mapMessage[0] = ""
        mapMessage[1] = ""
        mapMessage[2] = ""
        mapMessage[3] = ""
        mapMessage[4] = ""
        os.system('cls')  # clear screen for cmd for Windows OS
        os.system('clear')  # clear screen for cmd for Linux OS
        mapMessage[0] = "Already In Cave"
        legItem = -1
        legMessage = "Wumpus World Legend (not Legend of Zelda)"
        roomItem = -2
        printLegend(legMessage, legItem)
        drawMap(mapMessage, roomItem)

def option3():
    if playerClimb[0] == 1:
        mapMessage[0] = ""
        mapMessage[1] = ""
        mapMessage[2] = ""
        mapMessage[3] = ""
        mapMessage[4] = ""
        rotateLeft()
        playerScore[0] = playerScore[0] - 1  # -1 for turning
        _ascii = getPlayerRotation()
        wumpusMap[playerPosition[0]-1][-2] = chr(_ascii)  # sets the player rotation in map
        print(getPlayerRotation())
        os.system('cls')  # clear screen for cmd for Windows OS
        os.system('clear')  # clear screen for cmd for Linux OS
        legItem = -1
        legMessage = "Wumpus World Legend (not Legend of Zelda)"
        printLegend(legMessage, legItem)
        roomItem = -2
        drawMap(mapMessage, roomItem)
        # print(playerRotation[0])
    else:
        os.system('cls')  # clear screen for cmd for Windows OS
        os.system('clear')  # clear screen for cmd for Linux OS
        mapMessage[0] = ""
        mapMessage[1] = ""
        mapMessage[2] = ""
        mapMessage[3] = ""
        mapMessage[4] = ""
        mapMessage[0] = "Have to Climb Up First"
        legItem = -1
        legMessage = "Wumpus World Legend (not Legend of Zelda)"
        roomItem = -2
        printLegend(legMessage, legItem)
        drawMap(mapMessage, roomItem)

def option4():
    if playerClimb[0] == 1:
        mapMessage[0] = ""
        mapMessage[1] = ""
        mapMessage[2] = ""
        mapMessage[3] = ""
        mapMessage[4] = ""
        rotateRight()
        playerScore[0] = playerScore[0] - 1  # -1 for turning
        _ascii = getPlayerRotation()
        wumpusMap[playerPosition[0]-1][-2] = chr(_ascii)  # sets the player rotation in map
        print(getPlayerRotation())
        os.system('cls')  # clear screen for cmd for Windows OS
        os.system('clear')  # clear screen for cmd for Linux OS
        legItem = -1
        legMessage = "Wumpus World Legend (not Legend of Zelda)"
        printLegend(legMessage, legItem)
        roomItem = -2
        drawMap(mapMessage, roomItem)
    else:
        os.system('cls')  # clear screen for cmd for Windows OS
        os.system('clear')  # clear screen for cmd for Linux OS
        mapMessage[0] = ""
        mapMessage[1] = ""
        mapMessage[2] = ""
        mapMessage[3] = ""
        mapMessage[4] = ""
        mapMessage[0] = "Have to Climb Up First"
        legItem = -1
        legMessage = "Wumpus World Legend (not Legend of Zelda)"
        roomItem = -2
        printLegend(legMessage, legItem)
        drawMap(mapMessage, roomItem)

def option5():
    if playerClimb[0] == 1:
        getPlayerPosition()
        mapMessage[0] = ""
        mapMessage[1] = ""
        mapMessage[2] = ""
        mapMessage[3] = ""
        mapMessage[4] = ""
        moveForward()
        _ascii = getPlayerRotation()
        wumpusMap[playerPosition[0] - 1][-2] = chr(_ascii)  # place player on map
        print(getPlayerRotation())
        os.system('cls')  # clear screen for cmd for Windows OS
        os.system('clear')  # clear screen for cmd for Linux OS
        legItem = -1
        legMessage = "Wumpus World Legend (not Legend of Zelda)"
        printLegend(legMessage, legItem)
        roomItem = -2
        drawMap(mapMessage, roomItem)
        if playerWon[0] == 1:    
            print('\nThanks For Playing Wumpus World')
            print('You are a real winner.')
            exit()
        elif playerLost[0] == 1:
            print('\nThanks For Playing Wumpus World')
            print('Better Luck Next Time.')
            exit()
    else:
        os.system('cls')  # clear screen for cmd for Windows OS
        os.system('clear')  # clear screen for cmd for Linux OS
        mapMessage[0] = ""
        mapMessage[1] = ""
        mapMessage[2] = ""
        mapMessage[3] = ""
        mapMessage[4] = ""
        mapMessage[0] = "Have to Climb Up First"
        legItem = -1
        legMessage = "Wumpus World Legend (not Legend of Zelda)"
        roomItem = -2
        printLegend(legMessage, legItem)
        drawMap(mapMessage, roomItem)

def option6():
    if playerClimb[0] == 1:
        mapMessage[0] = ""
        mapMessage[1] = ""
        mapMessage[2] = ""
        mapMessage[3] = ""
        mapMessage[4] = ""
        if getPlayerArrows() > 0:
            shootArrow()
        else:
            mapMessage[0] = "Nothing to shoot with."
            mapMessage[1] = "No more Arrows."
            mapMessage[2] = ""

        _ascii = getPlayerRotation()
        wumpusMap[playerPosition[0] - 1][-2] = chr(_ascii)  # place player on map
        print(getPlayerRotation())
        os.system('cls')  # clear screen for cmd for Windows OS
        os.system('clear')  # clear screen for cmd for Linux OS
        legItem = -1
        legMessage = "Wumpus World Legend (not Legend of Zelda)"
        printLegend(legMessage, legItem)
        roomItem = -2
        drawMap(mapMessage, roomItem)
    else:
        os.system('cls')  # clear screen for cmd for Windows OS
        os.system('clear')  # clear screen for cmd for Linux OS
        mapMessage[0] = ""
        mapMessage[1] = ""
        mapMessage[2] = ""
        mapMessage[3] = ""
        mapMessage[4] = ""
        mapMessage[0] = "Have to Climb Up First"
        legItem = -1
        legMessage = "Wumpus World Legend (not Legend of Zelda)"
        roomItem = -2
        printLegend(legMessage, legItem)
        drawMap(mapMessage, roomItem)


def option7():
    if playerClimb[0] == 1:
        mapMessage[0] = ""
        mapMessage[1] = ""
        mapMessage[2] = ""
        mapMessage[3] = ""
        mapMessage[4] = ""
        playerHasGold[0] = pickupGold()
        _ascii = getPlayerRotation()
        wumpusMap[playerPosition[0] - 1][-2] = chr(_ascii)  # place player on map
        print(getPlayerRotation())
        os.system('cls')  # clear screen for cmd for Windows OS
        os.system('clear')  # clear screen for cmd for Linux OS
        legItem = -1
        legMessage = "Wumpus World Legend (not Legend of Zelda)"
        printLegend(legMessage, legItem)
        roomItem = -2
        drawMap(mapMessage, roomItem)
    else:
        os.system('cls')  # clear screen for cmd for Windows OS
        os.system('clear')  # clear screen for cmd for Linux OS
        mapMessage[0] = ""
        mapMessage[1] = ""
        mapMessage[2] = ""
        mapMessage[3] = ""
        mapMessage[4] = ""
        mapMessage[0] = "Have to Climb Up First"
        legItem = -1
        legMessage = "Wumpus World Legend (not Legend of Zelda)"
        roomItem = -2
        printLegend(legMessage, legItem)
        drawMap(mapMessage, roomItem)

if __name__ == '__main__':
    while (True):
        print_menu()
        
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        # Check what choice was entered and act accordingly

        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            option6()
        elif option == 7:
            option7()
        elif option == 8:
            print('Thanks For Playing Wumpus World')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 8.')
        







