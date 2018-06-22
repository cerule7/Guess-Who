import numpy as np
from gym.envs.guesswho.player import Player
from gym.envs.guesswho.gameboard import gameBoard
from gym.envs.guesswho.agent import Agent

class Game:

	p1 = None
	p2 = None
	numTurns = 0
	status = ''
	numFlipped = 0

	def __init__(self):
		sel = np.random.randint(0, 24)
		g1 = gameBoard(sel)
		self.p1 = Player("PLAYER 1", g1, sel)
		#self.p1 = Agent("Charlie", g1, sel)
		print(self.p1.getName() + " selected " + self.p1.getBoard().getCharacter(self.p1.getBoard().getSelected()).getName())
		j = np.random.randint(0, 24)
		g2 = gameBoard(j)
		#self.p2 = Player("PLAYER 2", g2, j)
		self.p2 = Agent("Alex", g2, j)
		print(self.p2.getName() + " selected " + self.p2.getBoard().getCharacter(self.p2.getBoard().getSelected()).getName())
		self.status = 'START'
		self.numFlipped = 0
		self.numTurns = 0
		self.gameOver = False

	# Resets game 
	def resetBoard(self):
		i = np.random.randint(0, 24)
		j = np.random.randint(0, 24)
		self.p1.selectedCharacter = i
		self.p2.selectedCharacter = j
		g1 = gameBoard(i)
		g2 = gameBoard(j)
		self.p1.setBoard(g1)
		self.p2.setBoard(g2)
		self.numTurns = 0
		self.status = 'START'
		self.numFlipped = 0
		self.gameOver = False
		print("RESET BOARD")


	def step(self): #returns status 
		if(self.status == 'WON' or self.status == 'LOST'):
			return self.status
		else:
			print("STATE NUMFLIPPED " + str(self.numFlipped))
			return str(self.numFlipped)

	def getState(self):
		m = self.p1.getBoard().numberActive()
		n = self.p2.getBoard().numberActive()
		return m, n

	def getAction(self, i, pturn):
		if pturn:
			player = self.p1
			otherplayer = self.p2
		else:
			player = self.p2
			otherplayer = self.p1
		#each number corresponds to an action 
		#auto quit (debug only)
		if i == -1:
			quit()
		#guess specific character
		elif i >= 0 and i < 24:
			if(i == otherplayer.getBoard().getSelected()):
				print("CORRECT GUESS")
				player.setScore(player.getScore() + 1)
				if pturn:
					self.status = 'WON'
				else:
					self.status = 'LOST'
			else:
				print("INCORRECT GUESS")
				otherplayer.setScore(otherplayer.getScore() + 1)
				if pturn:
					self.status = 'LOST'
				else:
					self.status = 'WON'
			return 
		#y/n questions
		elif i == 24:
			characterList, numFlipped = player.getBoard().askQ('isFemale', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
		elif i == 25:
			characterList, numFlipped = player.getBoard().askQ('hasHat', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
		elif i == 26:
			characterList, numFlipped = player.getBoard().askQ('hasGlasses', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
		elif i == 27:
			characterList, numFlipped = player.getBoard().askQ('hasBeard', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
		elif i == 28:
			characterList, numFlipped = player.getBoard().askQ('hasMustache', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
		elif i == 29:
			characterList, numFlipped = player.getBoard().askQ('hasRosyCheeks', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
		elif i == 30:
			characterList, numFlipped = player.getBoard().askQ('isSmiling', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
		elif i == 31:
			characterList, numFlipped = player.getBoard().askQ('isBald', otherplayer.getBoard())
			player.getBoard().updateList(characterList)
		#binary search
		elif i == 32:
			binaryPositions, characterlist, numFlipped = player.getBoard().binarySearch(player.getBinaryPositions(), otherplayer.getBoard())
			player.getBoard().updateList(characterlist)
			player.setBinaryPositions(binaryPositions)
		#hair colors
		else:
			characterlist, numFlipped = player.getBoard().askHairColor(i, otherplayer.getBoard())
			player.getBoard().updateList(characterlist)
		if pturn:
			self.p1 = player
			self.numFlipped = numFlipped
			print("NUMFLIPPED : " + str(self.numFlipped))
			self.state = self.numFlipped
		else:
			self.p2 = player

	def oneTurn(self, action): 
		#the bot/player goes 
		print(self.p1.getName() + " is guessing" + str(action))
		if(action >= 0 and action < 24):
			self.getAction(action, pturn=True)
			self.gameOver = True
		#for debug
		elif(action == -1):
			quit()
		else:
			self.getAction(action, pturn=True)
			print('P1 ACTIVE: ' + str(self.p1.getBoard().numberActive()))
			print('P2 ACTIVE: ' + str(self.p2.getBoard().numberActive()))
			if(self.p1.getBoard().numberActive() <= 1):
				self.p1.setScore(self.p1.getScore() + 1)
				print("PLAYER 1 WINS")
				self.status = 'WON'
				self.gameOver = True
		if(not self.gameOver):
			#the agent goes 
			action = 32
			print(self.p2.getName() + " is guessing" + str(action))
			#action = int(input("ACTION 1-40"))
			if(action >= 0 and action < 24):
				self.getAction(action, pturn=False)
				self.gameOver = True
			#for debug
			elif(action == -1):
				quit()
			else:
				self.getAction(action, pturn=False)
				print("P1 ACTIVE: " + str(self.p1.getBoard().numberActive()))
				print("P2 ACTIVE: " + str(self.p2.getBoard().numberActive()))
				if(self.p2.getBoard().numberActive() <= 1):
					self.p2.setScore(self.p2.getScore() + 1)
					print("PLAYER 2 WINS")
					self.status = 'LOST'
					self.gameOver = True

			self.numTurns += 1
			print("TOTAL TURNS: " + str(self.numTurns))