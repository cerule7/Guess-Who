import numpy as np
import random
import math
import gameboard
import character
from gym.envs.guesswho.player import Player
from gym.envs.guesswho.gameboard import gameBoard
from gym.envs.guesswho.optimalAgent import OptimalAgent


class Game:
    p1 = None
    p2 = None
    numTurns = 0
    status = ''
    numFlipped = 0
    agentType = ''  # agent types: binary, binaryp1, random, randomp1, demo,
    # none (self play), optimal (the paper agent)

    questions = {
        "0": "Is your character female?",
        "1": "Does your character have a hat?",
        "2": "Does your character have glasses?",
        "3": "Does your character have a beard?",
        "4": "Does your character have a mustache?",
        "5": "Does your character have rosy cheeks?",
        "6": "Is your character smiling?",
        "7": "Is your character bald?",
        "8": "Does your character have blue eyes?",
        "9": "Does your character have a big nose?",
        "10": "Does your character have a big mouth?",
        "11": "Does your character have earrings?",
        "12": "Does your character have a cleft chin?",
        "13": "[binary search]",
        "14": "Does your character have black hair?",
        "15": "Does your character have red hair?",
        "16": "Does your character have white hair?",
        "17": "Does your character have blond hair?",
        "18": "Does your character have brown hair?",
        "19": "Is your character Alex?",
        "20": "Is your character Alfred?",
        "21": "Is your character Anita?",
        "22": "Is your character Anne?",
        "23": "Is your character Bernard?",
        "24": "Is your character Bill?",
        "25": "Is your character Charles?",
        "26": "Is your character Claire?",
        "27": "Is your character David?",
        "28": "Is your character Eric?",
        "29": "Is your character Frans?",
        "30": "Is your character George?",
        "31": "Is your character Herman?",
        "32": "Is your character Joe?",
        "33": "Is your character Maria?",
        "34": "Is your character Max?",
        "35": "Is your character Paul?",
        "36": "Is your character Peter?",
        "37": "Is your character Philip?",
        "38": "Is your character Richard?",
        "39": "Is your character Robert?",
        "40": "Is your character Sam?",
        "41": "Is your character Susan?",
        "42": "Is your character Tom?"
    }

    def __init__(self):
        sel = np.random.randint(0, 24)
        g1 = gameBoard(sel)
        self.p1 = Player("PLAYER 1", g1, sel)
        print(self.p1.getName() + " selected " + self.p1.getBoard().getCharacter(
            self.p1.getBoard().getSelected()).getName())
        j = np.random.randint(0, 24)
        g2 = gameBoard(j)
        self.p2 = OptimalAgent("OPTIMAL ALEX", g2, j)
        print(self.p2.getName() + " selected " + self.p2.getBoard().getCharacter(
            self.p2.getBoard().getSelected()).getName())
        self.status = 'START'
        self.numFlipped = 0
        self.numTurns = 0
        self.gameOver = False
        # isFemale to hasButtchin + the five hair colors + m + n
        self.selTraits = np.zeros(21)

    def setAgentType(self, agentType):
        self.agentType = agentType
        print("AGENT TYPE IS " + self.agentType)

    def updateSelTraits(self, i, correct):
        if correct is False:
            self.selTraits[i] = -1
        else:
            self.selTraits[i] = 1

    def getNumTurns(self):
        return self.numTurns

    # Resets game 
    def resetBoard(self):
        i = np.random.randint(0, 24)
        j = np.random.randint(0, 24)
        self.p1.selectedCharacter = i
        self.p2.selectedCharacter = j
        g1 = gameBoard(i)
        g2 = gameBoard(j)
        self.p1.setBinaryPositions([0, 23])
        self.p2.setBinaryPositions([0, 23])
        self.p1.setBoard(g1)
        self.p2.setBoard(g2)
        self.numTurns = 0
        self.status = 'START'
        self.numFlipped = 0
        self.gameOver = False
        self.selTraits = np.zeros(21)
        print("RESET BOARD")

    def step(self):  # returns status
        if (self.status == 'WON' or self.status == 'LOST'):
            return self.status
        else:
            print("STATE NUMFLIPPED " + str(self.numFlipped))
            return str(self.numFlipped)

    def getState(self):
        self.selTraits[18] = self.p1.getBoard().numberActive()
        self.selTraits[19] = self.p2.getBoard().numberActive()
        n = int(self.p1.getBoard().numberActive())
        m = int(self.p2.getBoard().numberActive())

        # 2**k = 2**(log2(m-1))
        if (m - 1) > 0:
            k = math.floor(math.log((m - 1), 2))
            # player 1 is "in the weeds"
            if 2 ** (k + 1) <= n and 2 ** k <= m and m <= 2 ** (k + 1):
                self.selTraits[20] = -1
            else:
                self.selTraits[20] = 1
        else:
            self.selTraits[20] = 0

        return self.selTraits

    def getAction(self, i, pturn):
        i = int(i)
        if pturn:
            player = self.p1
            otherplayer = self.p2
        else:
            player = self.p2
            otherplayer = self.p1
        # each number corresponds to an action
        # auto quit (debug only)
        if i == -100:
            quit()
        # guessing specific characters
        elif i >= 19 and i <= 42:
            if i - 19 == otherplayer.getBoard().getSelected():
                print("CORRECT CHARACTER GUESS")
                self.status = 'WON'

                self.gameOver = True
            else:
                print("INCORRECT CHARACTER GUESS")
                cl = player.getBoard().getCharacterList()
                if cl[i - 19].isitActive():
                    cl[i - 19].setInactive()
                    player.getBoard().updateList(cl)
                    if pturn:
                        self.numFlipped = 1
                else:
                    if pturn:
                        self.numFlipped = 0

                self.status = self.numFlipped
            return
        # y/n questions
        elif i == 0:
            characterList, numFlipped = player.getBoard().askQ('isFemale', otherplayer.getBoard())
            player.getBoard().updateList(characterList)
            if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('isFemale'):
                self.updateSelTraits(0, True)
            elif pturn:
                self.updateSelTraits(0, False)
        elif i == 1:
            characterList, numFlipped = player.getBoard().askQ('hasHat', otherplayer.getBoard())
            player.getBoard().updateList(characterList)
            if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasHat'):
                self.updateSelTraits(1, True)
            elif pturn:
                self.updateSelTraits(1, False)
        elif i == 2:
            characterList, numFlipped = player.getBoard().askQ('hasGlasses', otherplayer.getBoard())
            player.getBoard().updateList(characterList)
            if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasGlasses'):
                self.updateSelTraits(2, True)
            elif pturn:
                self.updateSelTraits(2, False)
        elif i == 3:
            characterList, numFlipped = player.getBoard().askQ('hasBeard', otherplayer.getBoard())
            player.getBoard().updateList(characterList)
            if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasBeard'):
                self.updateSelTraits(3, True)
            elif pturn:
                self.updateSelTraits(3, False)
        elif i == 4:
            characterList, numFlipped = player.getBoard().askQ('hasMustache', otherplayer.getBoard())
            player.getBoard().updateList(characterList)
            if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasMustache'):
                self.updateSelTraits(4, True)
            elif pturn:
                self.updateSelTraits(4, False)
        elif i == 5:
            characterList, numFlipped = player.getBoard().askQ('hasRosyCheeks', otherplayer.getBoard())
            player.getBoard().updateList(characterList)
            if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasRosyCheeks'):
                self.updateSelTraits(5, True)
            elif pturn:
                self.updateSelTraits(5, False)
        elif i == 6:
            characterList, numFlipped = player.getBoard().askQ('isSmiling', otherplayer.getBoard())
            player.getBoard().updateList(characterList)
            if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('isSmiling'):
                self.updateSelTraits(6, True)
            elif pturn:
                self.updateSelTraits(6, False)
        elif i == 7:
            characterList, numFlipped = player.getBoard().askQ('isBald', otherplayer.getBoard())
            player.getBoard().updateList(characterList)
            if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('isBald'):
                self.updateSelTraits(7, True)
            elif pturn:
                self.updateSelTraits(7, False)
        elif i == 8:
            characterList, numFlipped = player.getBoard().askQ('hasBlueEyes', otherplayer.getBoard())
            player.getBoard().updateList(characterList)
            if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasBlueEyes'):
                self.updateSelTraits(8, True)
            elif pturn:
                self.updateSelTraits(8, False)
        elif i == 9:
            characterList, numFlipped = player.getBoard().askQ('hasBigNose', otherplayer.getBoard())
            player.getBoard().updateList(characterList)
            if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasBigNose'):
                self.updateSelTraits(9, True)
            elif pturn:
                self.updateSelTraits(9, False)
        elif i == 10:
            characterList, numFlipped = player.getBoard().askQ('hasBigMouth', otherplayer.getBoard())
            player.getBoard().updateList(characterList)
            if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasBigMouth'):
                self.updateSelTraits(10, True)
            elif pturn:
                self.updateSelTraits(10, False)
        elif i == 11:
            characterList, numFlipped = player.getBoard().askQ('hasEarrings', otherplayer.getBoard())
            player.getBoard().updateList(characterList)
            if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasEarrings'):
                self.updateSelTraits(11, True)
            elif pturn:
                self.updateSelTraits(11, False)
        elif i == 12:
            characterList, numFlipped = player.getBoard().askQ('hasButtchin', otherplayer.getBoard())
            player.getBoard().updateList(characterList)
            if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('hasButtchin'):
                self.updateSelTraits(12, True)
            elif pturn:
                self.updateSelTraits(12, False)
        # binary search
        elif i == 13:
            binaryPositions, characterlist, numFlipped = player.getBoard().binarySearch(player.getBinaryPositions(),
                                                                                        otherplayer.getBoard())
            player.getBoard().updateList(characterlist)
            player.setBinaryPositions(binaryPositions)
        # hair colors
        else:
            characterlist, numFlipped = player.getBoard().askHairColor(i, otherplayer.getBoard())
            player.getBoard().updateList(characterlist)
            if i == 14:
                if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('black'):
                    self.updateSelTraits(13, True)
                elif pturn:
                    self.updateSelTraits(13, False)
            if i == 15:
                if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('red'):
                    self.updateSelTraits(14, True)
                elif pturn:
                    self.updateSelTraits(14, False)
            if i == 16:
                if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('white'):
                    self.updateSelTraits(15, True)
                elif pturn:
                    self.updateSelTraits(15, False)
            if i == 17:
                if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('blonde'):
                    self.updateSelTraits(16, True)
                elif pturn:
                    self.updateSelTraits(16, False)
            else:
                if pturn and otherplayer.getBoard().getCharacter(otherplayer.getSelected()).hasAttribute('brown'):
                    self.updateSelTraits(17, True)
                elif pturn:
                    self.updateSelTraits(17, False)
        if pturn:
            self.p1 = player
            if self.agentType != 'randomp1' and self.agentType != 'binaryp1':
                self.numFlipped = numFlipped
                print("NUMFLIPPED : " + str(self.numFlipped))
                self.status = self.numFlipped
        elif not pturn:
            self.p2 = player
            if self.agentType == 'randomp1' or self.agentType == 'binaryp1':
                self.numFlipped = numFlipped
                print("NUMFLIPPED : " + str(self.numFlipped))
                self.status = self.numFlipped

    def agentPlay(self, action):
        action = abs(int(action))
        print("THE QNN asks: " + self.questions.get(str(action)))
        # for debug
        self.getAction(action, pturn=True)
        print('P1 ACTIVE: ' + str(self.p1.getBoard().numberActive()))
        print('P2 ACTIVE: ' + str(self.p2.getBoard().numberActive()))
        if (self.p1.getBoard().numberActive() <= 1):
            self.p1.setScore(self.p1.getScore() + 1)
            print("PLAYER 1 WINS")
            self.status = 'WON'
            self.gameOver = True
            return
        elif self.status == 'WON' or self.status == 'LOST':
            self.gameOver = True
            return
        # player 2 goes
        if self.gameOver != True:
            if (self.agentType == 'random'):
                action = random.randint(0, 18)
            elif (self.agentType == 'optimal'):
                action = int(
                    self.p2.makeOptimalGuess(self.p2.getBoard().numberActive(), self.p1.getBoard().numberActive()))
                print(action)
            elif (self.agentType == 'demo'):
                action = int(input('enter a # (0-18): '))
                while (action > 42 or action < 0):
                    action = int(input('enter a # (0-18): '))
            else:
                action = 13
            print(self.p2.getName() + " asks: " + self.questions.get(str(action)))
            self.getAction(action, pturn=False)
            print("P1 ACTIVE: " + str(self.p1.getBoard().numberActive()))
            print("P2 ACTIVE: " + str(self.p2.getBoard().numberActive()))
            if (self.p2.getBoard().numberActive() <= 1):
                self.p2.setScore(self.p2.getScore() + 1)
                print("PLAYER 2 WINS")
                self.status = 'LOST'
                self.gameOver = True
        self.numTurns += 1
        print("TOTAL TURNS: " + str(self.numTurns))

    def randomasP1(self, action):
        a = random.randint(0, 18)
        print("RANDOM BOT asks: " + self.questions.get(str(a)))
        # for debug
        self.getAction(a, pturn=True)
        print('P1 ACTIVE: ' + str(self.p1.getBoard().numberActive()))
        print('P2 ACTIVE: ' + str(self.p2.getBoard().numberActive()))
        if (self.p1.getBoard().numberActive() <= 1):
            self.p1.setScore(self.p1.getScore() + 1)
            print("PLAYER 1 WINS")
            self.status = 'LOST'
            self.gameOver = True
        # player 2 goes
        if self.gameOver != True:
            action = abs(int(action))
            print("THE QNN asks: " + self.questions.get(str(action)))
            self.getAction(action, pturn=False)
            print("P1 ACTIVE: " + str(self.p1.getBoard().numberActive()))
            print("P2 ACTIVE: " + str(self.p2.getBoard().numberActive()))
            if (self.p2.getBoard().numberActive() <= 1):
                self.p2.setScore(self.p2.getScore() + 1)
                print("PLAYER 2 WINS")
                self.status = 'WON'
                self.gameOver = True
        self.numTurns += 1
        print("TOTAL TURNS: " + str(self.numTurns))

    def binaryasP1(self, action):
        print("BINARY SEARCH BOT asks: " + self.questions.get(str(13)))
        # for debug
        if (action == -100):
            quit()
        else:
            self.getAction(13, pturn=True)
            print('P1 ACTIVE: ' + str(self.p1.getBoard().numberActive()))
            print('P2 ACTIVE: ' + str(self.p2.getBoard().numberActive()))
            if (self.p1.getBoard().numberActive() <= 1):
                self.p1.setScore(self.p1.getScore() + 1)
                print("PLAYER 1 WINS")
                self.status = 'LOST'
                self.gameOver = True
        if (self.gameOver != True):
            # player 1 goes
            action = abs(int(action))
            print("THE QNN asks: " + self.questions.get(str(action)))
            if (action == -100):
                quit()
            else:
                self.getAction(action, pturn=False)
                print("P1 ACTIVE: " + str(self.p1.getBoard().numberActive()))
                print("P2 ACTIVE: " + str(self.p2.getBoard().numberActive()))
                if (self.p2.getBoard().numberActive() <= 1):
                    self.p2.setScore(self.p2.getScore() + 1)
                    print("PLAYER 2 WINS")
                    self.status = 'WON'
                    self.gameOver = True
        self.numTurns += 1
        print("TOTAL TURNS: " + str(self.numTurns))

    def selfPlay(self, action):
        # the bot/player goes
        if (self.numTurns % 2 == 0):
            action = abs(int(action))
            print(self.p1.getName() + " asks: " + self.questions.get(str(action)))
            # for debug
            if (action == -100):
                quit()
            else:
                self.getAction(action, pturn=True)
                print('P1 ACTIVE: ' + str(self.p1.getBoard().numberActive()))
                print('P2 ACTIVE: ' + str(self.p2.getBoard().numberActive()))
                if (self.p1.getBoard().numberActive() <= 1):
                    self.p1.setScore(self.p1.getScore() + 1)
                    print("PLAYER 1 WINS")
                    self.status = 'WON'
                    self.gameOver = True
        else:
            # player 2 goes
            action = abs(int(action))
            print(self.p2.getName() + " asks: " + self.questions.get(str(action)))
            if (action == -100):
                quit()
            else:
                self.getAction(action, pturn=False)
                print("P1 ACTIVE: " + str(self.p1.getBoard().numberActive()))
                print("P2 ACTIVE: " + str(self.p2.getBoard().numberActive()))
                if (self.p2.getBoard().numberActive() <= 1):
                    self.p2.setScore(self.p2.getScore() + 1)
                    print("PLAYER 2 WINS")
                    self.status = 'LOST'
                    self.gameOver = True
        self.numTurns += 1
        print("TOTAL TURNS: " + str(self.numTurns))

    def oneTurn(self, action):
        if (self.agentType == 'none'):
            self.selfPlay(action)
        elif (self.agentType == 'binaryp1'):
            self.binaryasP1(action)
        elif (self.agentType == 'randomp1'):
            self.randomasP1(action)
        else:
            self.agentPlay(action)
